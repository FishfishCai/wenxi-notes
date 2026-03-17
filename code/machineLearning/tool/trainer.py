import json
import sys
from typing import Any
import warnings
from pathlib import Path
from timeit import default_timer
import torch
from torch import nn


# Only import wandb and use if installed
wandb_available = False
try:
    import wandb
    wandb_available = True
except ModuleNotFoundError:
    wandb_available = False

from .base_model import BaseModel


class Trainer:
    """
    Trains and evaluates a model with optional pre/post processing, checkpointing, and logging.
    """

    def __init__(
        self,
        *,
        model_class: BaseModel,
        config_path: str | Path,
        pre_processor: nn.Module = None,
        post_processor: nn.Module = None,
        n_epochs: int,
        device: str,
        mixed_precision: bool = False,
        eval_interval: int = 1,
        save_interval: int = 50,
        verbose: bool = True,
        wandb_log: bool = True,
        save_outputs: bool = False,
    ):
        """
        Build the trainer and load the model from a JSON config or a checkpoint.
        Optional pre_processor and post_processor are moved to ``device``; mixed precision is used only when ``device`` is CUDA.

        Parameters
        ----------
        model_class : BaseModel
            Class used to instantiate the model from ``config_path``.
        config_path : str or pathlib.Path
            Path to a ``.json`` (init args) or ``.pth`` (checkpoint) file.
        pre_processor : torch.nn.Module or None, optional
            Callable ``(inputs, gts) -> (inputs, gts)`` applied before the model; default None.
        post_processor : torch.nn.Module or None, optional
            Callable ``(outputs) -> outputs`` applied after the model; default None.
        n_epochs : int
            Number of epochs for :meth:`train`.
        device : str
            Device string for model and processors (e.g. ``"cuda:0"``).
        mixed_precision : bool, optional
            Use autocast and GradScaler when True and device is CUDA; default False.
        eval_interval : int, optional
            Run evaluation every this many epochs; default 1.
        save_interval : int, optional
            Save a checkpoint every this many epochs; default 50.
        verbose : bool, optional
            Print progress and checkpoint messages; default True.
        wandb_log : bool, optional
            Log metrics to W&B when available; default True.
        save_outputs : bool, optional
            Save last eval batch outputs each eval epoch; default False.

        Returns
        -------
        None
        """
        self.model_class = model_class
        self.n_epochs = n_epochs
        self.device = device
        self.resume_path = None

        self.pre_processor = pre_processor
        self.post_processor = post_processor
        if self.pre_processor is not None:
            self.pre_processor.to(self.device)
        if self.post_processor is not None:
            self.post_processor.to(self.device)

        ## Mixed precision only on CUDA
        use_amp = mixed_precision and "cuda" in self.device
        self.mixed_precision = use_amp
        self.autocast_device_type = "cuda" if use_amp else None
        self.scaler = torch.amp.GradScaler() if use_amp else None

        self.eval_interval = eval_interval
        self.save_interval = save_interval
        self.start_epoch = 0

        self.verbose = verbose

        # W&B: enable only if wandb is installed and a run is active
        self.wandb_log = False
        if wandb_available:
            self.wandb_log = wandb_log and wandb.run is not None

        self.save_outputs = save_outputs

        self.load_config(config_path)

    def load_config(self, config_path: str | Path):
        """
        Load the model from a JSON config or a checkpoint; set ``self.model`` and optionally ``self.resume_path``.

        Parameters
        ----------
        config_path : str or pathlib.Path
            Path to ``.json`` (constructor args) or ``.pth`` (state_dict + metadata).

        Returns
        -------
        None
        """
        path = Path(config_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Not found: {path}")

        suffix = path.suffix.lower()

        # JSON: build model from config dict and optional "args" list
        if suffix == ".json":
            cfg = json.loads(path.read_text(encoding="utf-8"))
            if cfg is not None and not isinstance(cfg, dict):
                raise TypeError(f"JSON root must be a dict, got {type(cfg)}")
            cfg = cfg or {}

            init_args = cfg.pop("args", []) or []
            if not isinstance(init_args, (list, tuple)):
                raise TypeError(f"'args' must be a list/tuple, got {type(init_args)}")

            cfg["mixed_precision"] = self.mixed_precision
            ## Instantiate model from config
            model = self.model_class(*init_args, **cfg)

        # .pth: restore model from state_dict and _metadata
        elif suffix == ".pth":
            self.resume_path = path
            ckpt = torch.load(path.as_posix(), map_location=self.device, weights_only=False)
            if not isinstance(ckpt, dict):
                raise TypeError(f"Checkpoint must be a dict, got {type(ckpt)}")
            if "model" not in ckpt or not isinstance(ckpt["model"], dict):
                raise KeyError('Checkpoint must contain a dict field "model" (model.state_dict()).')

            state = ckpt["model"]

            init_meta = state.get("_metadata")
            if not isinstance(init_meta, dict):
                raise ValueError('No "_metadata" found in ckpt["model"]; cannot reconstruct model.')

            model_name = init_meta.get("_name")
            if not model_name:
                raise ValueError('Checkpoint "_metadata" must contain "_name".')
            if self.model_class.__name__.lower() != model_name.lower():
                raise ValueError(
                    f'Model class name "{self.model_class.__name__}" does not match '
                    f'checkpoint model name "{model_name}".'
                )
            if self.verbose:
                print(f'Loading model "{model_name}" from checkpoint.')
                sys.stdout.flush()

            init_args = init_meta.get("args", []) or []
            if not isinstance(init_args, (list, tuple)):
                raise TypeError(f'metadata["args"] must be a list/tuple, got {type(init_args)}')
            init_kwargs = {k: v for k, v in init_meta.items() if k not in ("_name", "args")}
            init_kwargs["mixed_precision"] = self.mixed_precision
            ## Rebuild model from checkpoint metadata, then load state_dict
            model = self.model_class(*init_args, **init_kwargs)

        else:
            raise ValueError(f"Unsupported config file type: {suffix}")

        model.to(self.device)
        self.model = model

    def resume_state(self):
        """
        Load checkpoint from ``self.resume_path`` and restore epoch, model, optimizer, scheduler, and scaler state.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        ckpt = torch.load(self.resume_path.as_posix(), map_location=self.device, weights_only=False)
        if not isinstance(ckpt, dict):
            raise TypeError(f"Checkpoint must be a dict, got {type(ckpt)}")

        # Restore epoch index
        epoch = ckpt.get("epoch")
        if epoch is not None:
            print(f"Checkpoint was saved at epoch {epoch}.")
            self.start_epoch = int(epoch) + 1

        # Restore model/optimizer/scheduler/scaler from checkpoint keys
        if "model" in ckpt:
            if getattr(self, "model", None) is None:
                raise ValueError(
                    'Checkpoint has "model" but self.model is None. '
                    "Create model before calling resume_state()."
                )
            self.model.load_state_dict(ckpt["model"])

        # Restore optimizer state
        if "optimizer" in ckpt:
            if getattr(self, "optimizer", None) is None:
                raise ValueError(
                    'Checkpoint has "optimizer" but self.optimizer is None. '
                    "Create optimizer before calling resume_state()."
                )
            self.optimizer.load_state_dict(ckpt["optimizer"])

        # Restore scheduler state
        if "scheduler" in ckpt:
            if getattr(self, "scheduler", None) is None:
                raise ValueError(
                    'Checkpoint has "scheduler" but self.scheduler is None. '
                    "Create scheduler before calling resume_state()."
                )
            self.scheduler.load_state_dict(ckpt["scheduler"])

        # Restore mixed precision scaler
        if "scaler" in ckpt:
            if getattr(self, "scaler", None) is None:
                raise ValueError(
                    'Checkpoint has "scaler" but self.scaler is None. '
                    "Create scaler before calling resume_state()."
                )
            self.scaler.load_state_dict(ckpt["scaler"])

    def train(
        self,
        *,
        train_loader: object,
        eval_loaders: dict[str, object] = {},
        optimizer: torch.optim.Optimizer,
        scheduler: object = None,
        training_loss: nn.Module,
        eval_losses: dict[str, nn.Module] = {},
        save_dir: str | Path,
        save_loss: str = None,
        resume: bool = True,
    ):
        """
        Run the full training loop with evaluation and checkpointing; optionally resume from ``self.resume_path``.
        Best model is chosen by the metric named ``save_loss`` on the evaluation loaders.

        Parameters
        ----------
        train_loader : object
            Iterable of batches; each batch is a 2-tuple ``(inputs, gts)`` of dicts.
        eval_loaders : dict, optional
            Map loader name -> iterable of ``(inputs, gts)`` batches; default ``{}``.
        optimizer : torch.optim.Optimizer
            Optimizer for model parameters.
        scheduler : object
            LR scheduler; stepped with training error if ``ReduceLROnPlateau``.
        training_loss : callable
            Training loss; called as ``training_loss(**outputs, **gts)``, returns a scalar tensor.
        eval_losses : dict, optional
            Map metric name -> loss callable ``(**outputs, **gts) -> scalar``; default ``{}``.
        save_dir : str or pathlib.Path
            Directory for checkpoints and optional output files.
        save_loss : str or None, optional
            Key in ``eval_losses`` for best-model selection; if None, first key is used when eval_loaders non-empty.
        resume : bool, optional
            If True and ``self.resume_path`` is set, call :meth:`resume_state`; default True.

        Returns
        -------
        epoch_metrics : dict
            Metrics from the last epoch (e.g. train_err, avg_loss, epoch_train_time, and eval metrics).
        """
        self.optimizer = optimizer
        self.scheduler = scheduler

        # Warn if loss uses reduction="mean" (trainer expects sum over batch)
        if hasattr(training_loss, "reduction"):
            if training_loss.reduction == "mean":
                warnings.warn(
                    f"{training_loss.reduction=}. This means that the loss is "
                    "initialized to average across the batch dim. The Trainer "
                    "expects losses to sum across the batch dim."
                )
        for eval_loss in eval_losses.values():
            if hasattr(eval_loss, "reduction"):
                if eval_loss.reduction == "mean":
                    warnings.warn(
                        f"{eval_loss.reduction=}. This means that the loss is "
                        "initialized to average across the batch dim. The Trainer "
                        "expects losses to sum across the batch dim."
                    )

        # Default save_loss to first loader and first eval loss key
        if save_loss is None:
            if len(eval_loaders) == 0:
                self.save_loss = None
            else:
                save_loss_name = next(iter(eval_losses))
                save_loader_name = next(iter(eval_loaders))
                self.save_loss = f"{save_loader_name}_{save_loss_name}"
        else:
            self.save_loss = save_loss

        self.save_dir = Path(save_dir).expanduser().resolve()
        self.save_dir.mkdir(parents=True, exist_ok=True)

        if self.resume_path is not None and resume:
            self.resume_state()

        if self.verbose:
            msg = f"Training on {len(train_loader.dataset)} samples, "
            msg += f"evaluating on {len(eval_loaders)} loaders: "
            msg_parts = []
            for k, v in eval_loaders.items():
                msg_parts.append(f"{k}={len(v.dataset)} samples")
            msg += ", ".join(msg_parts)
            print(msg)
            sys.stdout.flush()

        best_metric_value = float("inf")

        # Main loop: train, optionally evaluate, save best and periodic checkpoints
        for epoch in range(self.start_epoch, self.n_epochs):
            train_err, avg_loss, epoch_train_time = self.train_one_epoch(epoch, train_loader, training_loss)

            epoch_metrics = dict[str, float](
                train_err=train_err,
                avg_loss=avg_loss,
                epoch_train_time=epoch_train_time,
            )

            if epoch % self.eval_interval == 0 and len(eval_loaders) > 0:
                eval_metrics = self.evaluate(
                    epoch=epoch,
                    eval_losses=eval_losses,
                    eval_loaders=eval_loaders,
                )
                epoch_metrics.update(**eval_metrics)

                if eval_metrics[self.save_loss] < best_metric_value:
                    best_metric_value = eval_metrics[self.save_loss]
                    self.save_state(
                        filename="best_model",
                        model=self.model,
                        optimizer=self.optimizer,
                        scheduler=self.scheduler,
                        scaler=self.scaler,
                        epoch=epoch,
                    )

            if (epoch + 1) % self.save_interval == 0:
                self.save_state(
                    filename=f"epoch_{epoch}",
                    model=self.model,
                    optimizer=self.optimizer,
                    scheduler=self.scheduler,
                    scaler=self.scaler,
                    epoch=epoch,
                )

        return epoch_metrics

    def train_one_epoch(self, epoch, train_loader, training_loss):
        """
        Train for one epoch: one forward/backward/step per batch; update scheduler; return mean loss and time.

        Parameters
        ----------
        epoch : int
            Current epoch index (for logging).
        train_loader : object
            Iterable of batches; each batch is a 2-tuple ``(inputs, gts)`` of dicts.
        training_loss : callable
            Called as ``training_loss(**outputs, **gts)``; returns a scalar tensor.

        Returns
        -------
        train_err : float
            Mean of ``loss.item()`` over batches.
        avg_loss : float
            Sum of ``loss.item()`` over batches divided by ``self.n_samples``.
        epoch_train_time : float
            Wall-clock seconds for the epoch.
        """
        avg_loss = 0
        train_err = 0.0
        t0 = default_timer()
        self.n_samples = 0

        self.model.train()
        # Processors in train mode (e.g. BatchNorm)
        if self.pre_processor is not None:
            self.pre_processor.train()
        if self.post_processor is not None:
            self.post_processor.train()

        for sample in train_loader:
            loss = self.train_one_batch(sample, training_loss)
            if self.scaler is not None:
                self.scaler.scale(loss).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                loss.backward()
                self.optimizer.step()

            train_err += loss.item()
            with torch.no_grad():
                avg_loss += loss.item()

        train_err /= len(train_loader)
        avg_loss /= self.n_samples

        if isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
            self.scheduler.step(train_err)
        elif self.scheduler is not None:
            self.scheduler.step()

        epoch_train_time = default_timer() - t0

        lr = None
        for pg in self.optimizer.param_groups:
            lr = pg["lr"]
        if self.verbose:
            self.log_training(
                epoch=epoch,
                time=epoch_train_time,
                avg_loss=avg_loss,
                train_err=train_err,
                lr=lr,
            )

        return train_err, avg_loss, epoch_train_time

    def evaluate(self, epoch, eval_loaders, eval_losses):
        """
        Compute evaluation metrics over all eval loaders and optionally save last-batch outputs.

        Parameters
        ----------
        epoch : int
            Current epoch (for logging and output filenames).
        eval_loaders : dict
            Map loader name -> iterable of ``(inputs, gts)`` batches.
        eval_losses : dict
            Map metric name -> callable ``(**outputs, **gts) -> scalar``.

        Returns
        -------
        eval_metrics : dict
            Map ``"{loader_name}_{loss_name}"`` -> mean loss per sample for that loader and metric.
        """
        self.model.eval()
        if self.pre_processor is not None:
            self.pre_processor.eval()
        if self.post_processor is not None:
            self.post_processor.eval()

        # Accumulate sums per (loader, loss); normalize by n_samples per loader
        eval_metrics = {}
        for loader_name in eval_loaders.keys():
            for loss_name in eval_losses.keys():
                eval_metrics[f"{loader_name}_{loss_name}"] = 0.0
        outs = []

        with torch.no_grad():
            for loader_name, eval_loader in eval_loaders.items():
                self.n_samples = 0
                for idx, sample in enumerate[Any](eval_loader):
                    return_output = (idx == len(eval_loader) - 1)
                    eval_step_losses, out = self.eval_one_batch(sample, eval_losses, return_output)
                    if return_output:
                        outs.append(out)
                    for loss_name, val_loss in eval_step_losses.items():
                        eval_metrics[f"{loader_name}_{loss_name}"] += val_loss
                for loss_name in eval_losses.keys():
                    eval_metrics[f"{loader_name}_{loss_name}"] /= self.n_samples

        if self.save_outputs:
            torch.save(
                outs,
                self.save_dir / f"outputs_epoch_{epoch}.pt",
            )

        if self.verbose:
            self.log_eval(epoch=epoch, eval_metrics=eval_metrics)
        return eval_metrics

    def train_one_batch(self, sample, training_loss):
        """
        Run one forward/backward step on a single batch; move data to device, apply pre/post_processor, return loss.

        Parameters
        ----------
        sample : object
            2-tuple ``(inputs, gts)`` of dicts; tensor values are moved to ``self.device``.
        training_loss : callable
            Called as ``training_loss(**outputs, **gts)``; returns a scalar tensor.

        Returns
        -------
        loss : torch.Tensor
            Scalar loss for this batch (for backward).
        """
        self.optimizer.zero_grad(set_to_none=True)

        inputs, gts = sample[0], sample[1]
        for k, v in inputs.items():
            if torch.is_tensor(v):
                inputs[k] = v.to(self.device, non_blocking=True)
        for k, v in gts.items():
            if torch.is_tensor(v):
                gts[k] = v.to(self.device, non_blocking=True)

        first_tensor = next((v for v in inputs.values() if torch.is_tensor(v)), None)
        if first_tensor is None:
            raise ValueError("The first input values must be torch Tensors.")
        self.n_samples += int(first_tensor.shape[0])

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        # Forward; post_processor and loss inside autocast when using mixed precision
        if self.mixed_precision:
            with torch.autocast(device_type=self.autocast_device_type):
                outputs = self.model(**inputs)
                if self.post_processor is not None:
                    outputs = self.post_processor(outputs)
                loss = training_loss(**outputs, **gts)
        else:
            outputs = self.model(**inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            loss = training_loss(**outputs, **gts)

        return loss

    def eval_one_batch(self, sample: dict, eval_losses: dict, return_output: bool = False):
        """
        Compute evaluation losses on one batch; no gradients. Optionally return postprocessed outputs.

        Parameters
        ----------
        sample : object
            2-tuple ``(inputs, gts)`` of dicts; tensors moved to ``self.device``.
        eval_losses : dict
            Map metric name -> callable ``(**outputs, **gts) -> scalar``.
        return_output : bool, optional
            If True, return the postprocessed ``outputs`` dict as second element; default False.

        Returns
        -------
        eval_step_losses : dict
            Map metric name -> float loss for this batch.
        outputs : dict or None
            Postprocessed model outputs if ``return_output`` is True; else None.
        """
        inputs, gts = sample[0], sample[1]
        for k, v in inputs.items():
            if torch.is_tensor(v):
                inputs[k] = v.to(self.device, non_blocking=True)
        for k, v in gts.items():
            if torch.is_tensor(v):
                gts[k] = v.to(self.device, non_blocking=True)

        first_tensor = next((v for v in inputs.values() if torch.is_tensor(v)), None)
        if first_tensor is None:
            raise ValueError("The first input values must be torch Tensors.")
        self.n_samples += int(first_tensor.shape[0])

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        # Forward and losses; post_processor inside autocast when mixed precision
        if self.mixed_precision:
            with torch.autocast(device_type=self.autocast_device_type):
                outputs = self.model(**inputs)
                if self.post_processor is not None:
                    outputs = self.post_processor(outputs)
                eval_step_losses = {}
                for loss_name, loss in eval_losses.items():
                    eval_step_losses[loss_name] = loss(**outputs, **gts).item()
        else:
            outputs = self.model(**inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            eval_step_losses = {
                loss_name: loss(**outputs, **gts).item()
                for loss_name, loss in eval_losses.items()
            }

        if return_output:
            # Move outputs to CPU for saving
            outputs = {k: (v.detach().cpu() if torch.is_tensor(v) else v) for k, v in outputs.items()}
            return eval_step_losses, outputs
        else:
            return eval_step_losses, None

    def log_training(
        self,
        epoch: int,
        time: float,
        avg_loss: float,
        train_err: float,
        lr: float = None,
    ):
        """
        Print training metrics (epoch, time, avg_loss, train_err, lr) and optionally log to W&B.

        Parameters
        ----------
        epoch : int
            Epoch index (logging step).
        time : float
            Epoch wall-clock time in seconds.
        avg_loss : float
            Mean training loss per sample for the epoch.
        train_err : float
            Mean training loss per batch for the epoch.
        lr : float or None, optional
            Learning rate from the last optimizer param group; default None.

        Returns
        -------
        None
        """
        if self.wandb_log:
            values_to_log = dict[str, float | None](
                train_err=train_err,
                time=time,
                avg_loss=avg_loss,
                lr=lr,
            )

        msg = f"[{epoch}] time={time:.2f}, "
        msg += f"avg_loss={avg_loss:.4f}, "
        msg += f"train_err={train_err:.4f}, "
        msg += f"lr={lr:.3e}" if lr is not None else "lr=N/A"

        print(msg)
        sys.stdout.flush()

        if self.wandb_log:
            wandb.log(data=values_to_log, step=epoch + 1, commit=False)

    def log_eval(self, epoch: int, eval_metrics: dict):
        """
        Print evaluation metrics (one per line) and optionally log them to W&B.

        Parameters
        ----------
        epoch : int
            Epoch index (logging step).
        eval_metrics : dict
            Map metric name -> float or scalar tensor.

        Returns
        -------
        None
        """
        values_to_log = {}
        for idx, (metric, value) in enumerate[tuple](eval_metrics.items()):
            if isinstance(value, float) or isinstance(value, torch.Tensor):
                if idx == 0:
                    print(f"Eval: {metric}={value:.4f}")
                else:
                    print(f"      {metric}={value:.4f}")
            if self.wandb_log:
                values_to_log[metric] = value

        sys.stdout.flush()

        if self.wandb_log:
            wandb.log(data=values_to_log, step=epoch + 1, commit=True)

    def save_state(
        self,
        filename: str,
        model: nn.Module,
        optimizer: torch.optim.Optimizer = None,
        scheduler: object = None,
        scaler: torch.amp.GradScaler = None,
        epoch: int = None,
    ):
        """
        Save a checkpoint to ``self.save_dir/{filename}.pth`` with model state and optional optimizer/scheduler/scaler/epoch.

        Parameters
        ----------
        filename : str
            Base filename (no suffix); file is ``{filename}.pth``.
        model : torch.nn.Module
            Model; its state dict is stored under key ``"model"``.
        optimizer : torch.optim.Optimizer or None, optional
            Stored under ``"optimizer"`` if provided; default None.
        scheduler : object or None, optional
            Stored under ``"scheduler"`` if provided; default None.
        scaler : torch.amp.GradScaler or None, optional
            Stored under ``"scaler"`` if provided; default None.
        epoch : int or None, optional
            Stored under ``"epoch"`` if provided; default None.

        Returns
        -------
        None
        """
        save_path = self.save_dir / f"{filename}.pth"

        ckpt = {"model": model.state_dict()}

        if optimizer is not None:
            ckpt["optimizer"] = optimizer.state_dict()

        if scheduler is not None:
            ckpt["scheduler"] = scheduler.state_dict()

        if scaler is not None:
            ckpt["scaler"] = scaler.state_dict()

        if epoch is not None:
            ckpt["epoch"] = int(epoch)

        torch.save(ckpt, save_path.as_posix())

        if self.verbose:
            print(f"Saved training state to {save_path}")
            sys.stdout.flush()
