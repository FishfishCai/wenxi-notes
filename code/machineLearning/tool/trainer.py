import json
import sys
from typing import Any
import warnings
from pathlib import Path
from timeit import default_timer
import torch
from torch import nn

from .base_model import BaseModel


class Trainer:
    """
    Orchestrates model training, evaluation, checkpointing, and optional file logging.
    """

    def __init__(
        self,
        *,
        model_class: BaseModel,
        pre_processor: nn.Module = None,
        post_processor: nn.Module = None,
        config_path: str | Path,
        resume: bool = True,
        n_epochs: int,
        device: str,
        mixed_precision: bool = False,
        eval_interval: int = 1,
        save_interval: int = 50,
        verbose: bool = True,
        save_logs: bool = False,
        save_outs: bool = False,
    ):
        """
        Load ``self.model`` from ``config_path``, move modules to ``device``, and optionally restore
        training state from the same path when ``resume`` is True.

        Parameters
        ----------
        model_class : BaseModel
            Class used to instantiate the model from ``config_path``.
        pre_processor : torch.nn.Module or None, optional
            Module applied as ``(inputs, gts) -> (inputs, gts)`` before the forward pass; default None.
        post_processor : torch.nn.Module or None, optional
            Module applied as ``(outputs) -> outputs`` after the forward pass; default None.
        config_path : str or pathlib.Path
            Path to ``.json`` (constructor kwargs and optional positional ``args``) or ``.pth`` (checkpoint with ``model`` state).
        resume : bool, optional
            If True, call :meth:`resume_state` with ``config_path`` after :meth:`load_config`; default True.
        n_epochs : int
            Number of epochs to run in :meth:`train`.
        device : str
            Device string for the model and processors (e.g. ``"cuda:0"``).
        mixed_precision : bool, optional
            If True and ``device`` contains ``"cuda"``, enable autocast and a ``GradScaler``; default False.
        eval_interval : int, optional
            In :meth:`train`, run :meth:`evaluate` every this many epochs; default 1.
        save_interval : int, optional
            In :meth:`train`, save a periodic checkpoint every this many completed epochs; default 50.
        verbose : bool, optional
            If True, print training summaries and checkpoint paths; default True.
        save_logs : bool, optional
            If True, :meth:`train` sets ``self.log_dir`` to ``save_dir / "logs.txt"`` and appends lines via :meth:`log_train` and :meth:`log_eval`; default False.
        save_outs : bool, optional
            If True, :meth:`evaluate` saves collected last-batch outputs under ``self.save_dir``; default False.

        Returns
        -------
        None
        """
        self.model_class = model_class
        self.n_epochs = n_epochs
        self.device = device

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
        self.save_logs = save_logs
        self.save_outs = save_outs

        self.load_config(config_path)
        if resume:
            self.resume_state(config_path)

    def load_config(self, config_path: str | Path):
        """
        Construct ``self.model`` from a ``.json`` config or from ``_metadata`` embedded in a ``.pth`` checkpoint,
        then move the model to ``self.device``. For ``.json``, ``mixed_precision`` from the trainer overrides the file.

        Parameters
        ----------
        config_path : str or pathlib.Path
            Existing path with suffix ``.json`` (root dict, optional list key ``args`` for positional ctor args) or ``.pth`` (dict with ``model`` state dict containing ``_metadata``).

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
                print(f'Loading config of model "{model_name}" from checkpoint.')
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

    def resume_state(self, resume_path: str | Path):
        """
        Load a ``.pth`` training checkpoint from ``resume_path`` and restore ``start_epoch`` plus any present
        ``model``, ``optimizer``, ``scheduler``, and ``scaler`` state dicts into existing attributes.

        Parameters
        ----------
        resume_path : str or pathlib.Path
            Checkpoint file loaded with ``torch.load`` and ``map_location=self.device``.

        Returns
        -------
        None
        """
        ckpt = torch.load(resume_path.as_posix(), map_location=self.device, weights_only=False)
        if not isinstance(ckpt, dict):
            raise TypeError(f"Checkpoint must be a dict, got {type(ckpt)}")

        # Restore epoch index
        epoch = ckpt.get("epoch")
        if epoch is not None:
            print(f"Loading checkpoint from epoch {epoch}.")
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
        save_loss: str = None
    ):
        """
        Run epochs from ``self.start_epoch`` to ``self.n_epochs``-1, optionally evaluate, save the best checkpoint
        by ``self.save_loss``, and save periodic checkpoints under ``save_dir``.

        Parameters
        ----------
        train_loader : object
            Iterable of batches; each batch is ``(inputs, gts)`` with dict-valued tensors (batch size ``N`` on the first tensor dim).
        eval_loaders : dict[str, object], optional
            Names mapped to iterables of ``(inputs, gts)`` batches; default empty dict skips evaluation.
        optimizer : torch.optim.Optimizer
            Optimizer updated in :meth:`train_one_batch` / :meth:`train_one_epoch`.
        scheduler : object or None, optional
            If ``ReduceLROnPlateau``, stepped with mean batch loss; else if not None, stepped once per epoch; default None.
        training_loss : torch.nn.Module
            Scalar loss module called as ``training_loss(**outputs, **gts)``; batch terms should sum over batch (not ``reduction="mean"``).
        eval_losses : dict[str, torch.nn.Module], optional
            Metric names mapped to scalar loss modules ``(**outputs, **gts)``; default empty dict.
        save_dir : str or pathlib.Path
            Root directory for ``.pth`` checkpoints, optional ``logs.txt`` when ``save_logs``, and eval output ``.pt`` files when ``save_outs``.
        save_loss : str or None, optional
            Key matching ``"{loader}_{loss_name}"`` in eval metrics for best checkpoint; if None and ``eval_loaders`` non-empty, defaults to first loader and first eval loss name.

        Returns
        -------
        None
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
        if self.save_logs:
            log_txt = self.save_dir / "logs.txt"
            if not log_txt.is_file():
                log_txt.touch()
            self.log_dir = log_txt

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
            self.train_one_epoch(epoch, train_loader, training_loss)

            if epoch % self.eval_interval == 0 and len(eval_loaders) > 0:
                eval_metrics = self.evaluate(epoch, eval_losses, eval_loaders)

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

    def train_one_epoch(self, epoch, train_loader, training_loss):
        """
        Run one pass over ``train_loader``, accumulate ``train_err`` (mean per-batch loss) and ``avg_loss`` (mean per sample),
        step ``scheduler`` if set, then print and optionally append the same line to ``self.log_dir``.

        Parameters
        ----------
        epoch : int
            Epoch index passed to :meth:`print_train` / :meth:`log_train`.
        train_loader : object
            Iterable of ``(inputs, gts)`` batches; ``len(train_loader)`` used to normalize ``train_err``.
        training_loss : torch.nn.Module
            Scalar loss module used inside :meth:`train_one_batch`.

        Returns
        -------
        None
        """
        avg_loss = 0
        train_err = 0.0
        t0 = default_timer()
        self.n_samples = 0

        self.model.train()
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
            self.print_train(epoch, epoch_train_time, avg_loss, train_err, lr)
        if self.save_logs:
            self.log_train(epoch, epoch_train_time, avg_loss, train_err, lr)

    def evaluate(self, epoch, eval_loaders, eval_losses):
        """
        For each named loader, sum per-batch ``.item()`` losses per metric, normalize by total samples ``self.n_samples`` for that loader,
        optionally save stacked last-batch CPU outputs, then print and optionally log one eval line.

        Parameters
        ----------
        epoch : int
            Epoch index for :meth:`print_eval` / :meth:`log_eval` and for ``outputs_epoch_{epoch}.pt`` when ``save_outs``.
        eval_loaders : dict[str, object]
            Loader names mapped to iterables of ``(inputs, gts)`` batches with consistent batch-size tensors.
        eval_losses : dict[str, torch.nn.Module]
            Metric names mapped to scalar loss modules evaluated in :meth:`eval_one_batch`.

        Returns
        -------
        eval_metrics : dict[str, float]
            Keys ``f"{loader_name}_{loss_name}"`` mapping to mean loss per sample for that loader.
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

        if self.save_outs:
            torch.save(outs, self.save_dir / f"outputs_epoch_{epoch}.pt")

        if self.verbose:
            self.print_eval(epoch, eval_metrics)
        if self.save_logs:
            self.log_eval(epoch, eval_metrics)
        return eval_metrics

    def train_one_batch(self, sample, training_loss):
        """
        Move batch tensors to ``self.device``, optionally apply ``pre_processor``, forward through ``model`` and ``post_processor``
        (inside autocast when mixed precision), and return a scalar ``loss`` without calling ``backward``.

        Parameters
        ----------
        sample : object
            ``(inputs, gts)`` dicts; first tensor in ``inputs`` supplies batch size ``N`` for ``self.n_samples``.
        training_loss : torch.nn.Module
            Scalar loss ``training_loss(**outputs, **gts)``.

        Returns
        -------
        loss : torch.Tensor
            Scalar tensor (shape ``()``) for backward in the training loop.
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
        Run eval-mode forward (no backward), record each metric as a Python float ``.item()``, and optionally return
        CPU-detached postprocessed ``outputs`` for saving.

        Parameters
        ----------
        sample : object
            ``(inputs, gts)`` dicts with the same layout as training; batch size taken from the first tensor in ``inputs``.
        eval_losses : dict[str, torch.nn.Module]
            Metric names mapped to scalar loss modules.
        return_output : bool, optional
            If True, second return value is a dict of tensors moved to CPU; if False, second value is None; default False.

        Returns
        -------
        eval_step_losses : dict[str, float]
            Per-metric scalar batch losses (summed terms as returned by each module).
        outputs : dict or None
            Postprocessed outputs on CPU if ``return_output`` is True; otherwise None.
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

    def print_train(
        self,
        epoch: int,
        time: float,
        avg_loss: float,
        train_err: float,
        lr: float = None,
    ):
        """
        Format one line ``[epoch] time=... avg_loss=... train_err=... lr=...`` and print it with flushed stdout.

        Parameters
        ----------
        epoch : int
            Epoch index shown in brackets.
        time : float
            Wall-clock seconds for the epoch.
        avg_loss : float
            Mean loss per sample (total loss sum divided by ``self.n_samples``).
        train_err : float
            Mean per-batch ``loss.item()`` over the epoch.
        lr : float or None, optional
            Last param-group learning rate, or None to print ``lr=N/A``; default None.

        Returns
        -------
        None
        """
        msg = f"[{epoch}] time={time:.2f}, "
        msg += f"avg_loss={avg_loss:.4f}, "
        msg += f"train_err={train_err:.4f}, "
        msg += f"lr={lr:.3e}" if lr is not None else "lr=N/A"
        print(msg)
        sys.stdout.flush()

    def print_eval(self, epoch: int, eval_metrics: dict):
        """
        Build ``[Eval epoch] m1=v1, m2=v2, ...`` from float or 0-d tensor values, print one line, and flush stdout.

        Parameters
        ----------
        epoch : int
            Epoch index in the prefix.
        eval_metrics : dict
            Metric name to ``float`` or scalar ``torch.Tensor``; entries that are neither are skipped.

        Returns
        -------
        None
        """
        msg = f"[Eval {epoch}] "
        parts = []
        for metric, value in eval_metrics.items():
            if isinstance(value, float) or isinstance(value, torch.Tensor):
                v = float(value.item()) if isinstance(value, torch.Tensor) else float(value)
                parts.append(f"{metric}={v:.4f}")
        msg += ", ".join(parts)
        print(msg)
        sys.stdout.flush()

    def log_train(
        self,
        epoch: int,
        time: float,
        avg_loss: float,
        train_err: float,
        lr: float = None,
    ):
        """
        Append the same single-line message as :meth:`print_train` to ``self.log_dir`` (UTF-8, newline-terminated).

        Parameters
        ----------
        epoch : int
            Epoch index in the log line.
        time : float
            Wall-clock seconds for the epoch.
        avg_loss : float
            Mean loss per sample for the epoch.
        train_err : float
            Mean per-batch loss for the epoch.
        lr : float or None, optional
            Learning rate string as in :meth:`print_train`; default None.

        Returns
        -------
        None
        """
        msg = f"[{epoch}] time={time:.2f}, "
        msg += f"avg_loss={avg_loss:.4f}, "
        msg += f"train_err={train_err:.4f}, "
        msg += f"lr={lr:.3e}" if lr is not None else "lr=N/A"
        with self.log_dir.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")

    def log_eval(self, epoch: int, eval_metrics: dict):
        """
        Append the same single-line message as :meth:`print_eval` to ``self.log_dir`` (UTF-8, newline-terminated).

        Parameters
        ----------
        epoch : int
            Epoch index in the prefix.
        eval_metrics : dict
            Same keys and value types as accepted by :meth:`print_eval`.

        Returns
        -------
        None
        """
        msg = f"[Eval {epoch}] "
        parts = []
        for metric, value in eval_metrics.items():
            if isinstance(value, float) or isinstance(value, torch.Tensor):
                v = float(value.item()) if isinstance(value, torch.Tensor) else float(value)
                parts.append(f"{metric}={v:.4f}")
        msg += ", ".join(parts)
        with self.log_dir.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")

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
        Write ``torch.save`` dict to ``self.save_dir / f"{filename}.pth"`` with at least ``"model"`` state and optional
        optimizer, scheduler, scaler, and integer epoch for :meth:`resume_state`.

        Parameters
        ----------
        filename : str
            Base name without ``.pth``; full path is under ``self.save_dir``.
        model : torch.nn.Module
            Module whose ``state_dict()`` is stored as ``ckpt["model"]``.
        optimizer : torch.optim.Optimizer or None, optional
            If not None, ``state_dict`` stored as ``"optimizer"``; default None.
        scheduler : object or None, optional
            If not None, ``scheduler.state_dict()`` stored as ``"scheduler"``; default None.
        scaler : torch.amp.GradScaler or None, optional
            If not None, AMP scaler state stored as ``"scaler"``; default None.
        epoch : int or None, optional
            If not None, stored as integer ``ckpt["epoch"]``; default None.

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
