import json
import sys
import warnings
from pathlib import Path
from timeit import default_timer
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union
import torch
from torch import nn

from .base_model import BaseModel


class Trainer:
    """Orchestrates training, evaluation, checkpointing, and optional log files."""

    def __init__(
        self,
        *,
        model_class: Type[BaseModel],
        pre_processor: Optional[nn.Module] = None,
        post_processor: Optional[nn.Module] = None,
        config_path: Union[str, Path],
        save_dir: Optional[Union[Path, str]],
        resume: bool = True,
        n_epochs: int,
        device: str,
        mixed_precision: bool = False,
        eval_interval: int = 1,
        save_interval: int = 50,
        verbose: bool = True,
        save_logs: bool = True,
        save_outs: bool = False,
        save_inputs: bool = False,
        save_gts: bool = False,
        n_outs: Optional[int] = None,
    ) -> None:
        """
        Build ``self.model`` from ``config_path``, move modules to ``device``, and optionally resume training state.

        Parameters
        ----------
        model_class : type of BaseModel
            Class used to construct ``self.model`` from JSON or checkpoint ``_metadata``.
        pre_processor : torch.nn.Module or None, optional
            Applied as ``(inputs, gts) -> (inputs, gts)`` before the forward pass. Default is None.
        post_processor : torch.nn.Module or None, optional
            Applied as ``(outputs) -> outputs`` after the forward pass. Default is None.
        config_path : str or pathlib.Path
            ``.json`` file (constructor kwargs and optional ``args`` list) or ``.pth`` with ``model`` and ``_metadata``.
        resume : bool, optional
            If True, call :meth:`resume_state` after :meth:`load_config`. Default is True.
        n_epochs : int
            Exclusive upper epoch index passed to :meth:`train` (loops ``range(self.start_epoch, n_epochs)``).
        device : str
            Device string for the model and processors (for example ``"cuda:0"`` or ``"cpu"``).
        mixed_precision : bool, optional
            If True and ``device`` contains ``"cuda"``, enable autocast and ``GradScaler``. Default is False.
        eval_interval : int, optional
            Run :meth:`evaluate` every this many epochs inside :meth:`train`. Default is 1.
        save_interval : int, optional
            Save a periodic checkpoint every this many completed epochs in :meth:`train`. Default is 50.
        verbose : bool, optional
            If True, print training and checkpoint messages. Default is True.
        save_logs : bool, optional
            If True, append lines to ``save_dir / "logs.txt"`` via :meth:`log_train` and :meth:`log_eval`. Default is False.
        save_outs : bool, optional
            If True, :meth:`evaluate` saves outputs under ``self.save_dir``. Default is False.
        save_inputs : bool, optional
            If True, :meth:`evaluate` saves inputs under ``self.save_dir``. Default is False.
        save_gts : bool, optional
            If True, :meth:`evaluate` saves ground truths under ``self.save_dir``. Default is False.
        n_outs : int or None, optional
            Maximum number of samples to keep when saving outputs/inputs/gts. None means no limit. Default is None.

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

        ## AMP only when CUDA is selected
        use_amp = mixed_precision and "cuda" in self.device
        self.mixed_precision = use_amp
        self.autocast_device_type = "cuda" if use_amp else None
        self.scaler = torch.amp.GradScaler() if use_amp else None

        self.eval_interval = eval_interval
        self.save_interval = save_interval
        self.start_epoch = 0

        self.verbose = verbose
        self.save_dir = Path(save_dir).expanduser().resolve()
        self.save_logs = save_logs
        self.save_outs = save_outs
        self.save_inputs = save_inputs
        self.save_gts = save_gts
        self.n_outs = n_outs

        self.load_config(config_path)
        if resume and Path(config_path).suffix == ".pth":
            self.resume_state(config_path)

    def load_config(
        self,
        config_path: Union[str, Path],
    ) -> None:
        """
        Instantiate ``self.model`` from a ``.json`` config or from ``_metadata`` inside a ``.pth`` checkpoint.

        Parameters
        ----------
        config_path : str or pathlib.Path
            Existing ``.json`` (root dict, optional ``args`` list) or ``.pth`` (dict with ``model`` state and ``_metadata``).

        Returns
        -------
        None
        """
        path = Path(config_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Not found: {path}")

        suffix = path.suffix.lower()

        # JSON path: optional positional ``args`` plus kwargs
        if suffix == ".json":
            cfg = json.loads(path.read_text(encoding="utf-8"))
            if cfg is not None and not isinstance(cfg, dict):
                raise TypeError(f"JSON root must be a dict, got {type(cfg)}")
            cfg = cfg or {}

            init_args = cfg.pop("args", []) or []
            if not isinstance(init_args, (list, tuple)):
                raise TypeError(f"'args' must be a list/tuple, got {type(init_args)}")

            cfg["mixed_precision"] = self.mixed_precision
            ## Model from JSON
            model = self.model_class(*init_args, **cfg)

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
            ## Model from checkpoint metadata, then weights
            model = self.model_class(*init_args, **init_kwargs)

        else:
            raise ValueError(f"Unsupported config file type: {suffix}")

        model.to(self.device)
        self.model = model

    def resume_state(
        self,
        resume_path: Union[str, Path],
    ) -> None:
        """
        Load a ``.pth`` checkpoint and restore ``start_epoch`` and any ``model``, ``optimizer``, ``scheduler``, and ``scaler`` state.

        Parameters
        ----------
        resume_path : str or pathlib.Path
            File passed to ``torch.load`` with ``map_location=self.device``.

        Returns
        -------
        None
        """
        ckpt = torch.load(Path(resume_path).as_posix(), map_location=self.device, weights_only=False)
        if not isinstance(ckpt, dict):
            raise TypeError(f"Checkpoint must be a dict, got {type(ckpt)}")

        # ``epoch`` -> ``self.start_epoch``
        epoch = ckpt.get("epoch")
        if epoch is not None:
            print(f"Loading checkpoint from epoch {epoch}.")
            self.start_epoch = int(epoch) + 1

        if "model" in ckpt:
            if getattr(self, "model", None) is None:
                raise ValueError(
                    'Checkpoint has "model" but self.model is None. '
                    "Create model before calling resume_state()."
                )
            self.model.load_state_dict(ckpt["model"])

        if "optimizer" in ckpt:
            if getattr(self, "optimizer", None) is None:
                raise ValueError(
                    'Checkpoint has "optimizer" but self.optimizer is None. '
                    "Create optimizer before calling resume_state()."
                )
            self.optimizer.load_state_dict(ckpt["optimizer"])

        if "scheduler" in ckpt:
            if getattr(self, "scheduler", None) is None:
                raise ValueError(
                    'Checkpoint has "scheduler" but self.scheduler is None. '
                    "Create scheduler before calling resume_state()."
                )
            self.scheduler.load_state_dict(ckpt["scheduler"])

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
        eval_loaders: Dict[str, object] = {},
        optimizer: torch.optim.Optimizer,
        scheduler: Optional[object] = None,
        train_losses: Union[nn.Module, Dict[str, nn.Module]],
        backward_loss: Optional[str] = None,
        eval_losses: Union[nn.Module, Dict[str, nn.Module]] = {},
        save_loss: Optional[str] = None,
    ) -> None:
        """
        Run training epochs with optional evaluation, best checkpointing by ``self.save_loss``, and periodic saves.

        Parameters
        ----------
        train_loader : object
            Iterable of ``(inputs, gts)`` batches; tensors are dict-valued with batch size on dimension 0.
        eval_loaders : dict of str to object
            Loader names to iterables of ``(inputs, gts)`` batches; empty dict skips evaluation.
        optimizer : torch.optim.Optimizer
            Optimizer stepped in :meth:`_train_one_batch` / :meth:`train_one_epoch`.
        scheduler : object or None, optional
            ``ReduceLROnPlateau`` is stepped with the mean batch loss; any other non-None scheduler is stepped once per epoch. Default is None.
        train_losses : torch.nn.Module or dict of str to torch.nn.Module
            A single loss module or named loss modules ``loss(**outputs, **gts)``; all are computed and logged each batch.
            A single module is wrapped as ``{"loss": module}``.
        backward_loss : str or None, optional
            Key in ``train_losses`` whose output is back-propagated. If None, defaults to the first key. Default is None.
        eval_losses : torch.nn.Module or dict of str to torch.nn.Module
            A single metric module or named metric modules ``(**outputs, **gts)``.
            A single module is wrapped as ``{"loss": module}``.
        save_loss : str or None, optional
            Key ``f"{loader}_{loss_name}"`` used for the best checkpoint; if None and ``eval_loaders`` is non-empty, defaults to the first loader and first metric. Default is None.

        Returns
        -------
        None
        """
        self.optimizer = optimizer
        self.scheduler = scheduler

        if isinstance(train_losses, nn.Module):
            train_losses = {"loss": train_losses}
        if isinstance(eval_losses, nn.Module):
            eval_losses = {"loss": eval_losses}

        if backward_loss is None:
            backward_loss = next(iter(train_losses))
        if backward_loss not in train_losses:
            raise KeyError(
                f'backward_loss="{backward_loss}" is not a key in train_losses '
                f"(available: {list(train_losses.keys())})"
            )

        # ``reduction="mean"`` conflicts with trainer batch-sum convention
        for train_loss in train_losses.values():
            if hasattr(train_loss, "reduction"):
                if train_loss.reduction == "mean":
                    warnings.warn(
                        f"{train_loss.reduction=}. This means that the loss is "
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

        if save_loss is None:
            if len(eval_loaders) == 0:
                self.save_loss = None
            else:
                save_loss_name = next(iter(eval_losses))
                save_loader_name = next(iter(eval_loaders))
                self.save_loss = f"{save_loader_name}_{save_loss_name}"
        else:
            self.save_loss = save_loss

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

        # Epoch loop with eval and checkpoints
        for epoch in range(self.start_epoch, self.n_epochs):
            self.train_one_epoch(epoch, train_loader, train_losses, backward_loss)

            if epoch % self.eval_interval == 0 and len(eval_loaders) > 0:
                eval_metrics = self.evaluate(
                    eval_loaders,
                    eval_losses,
                    epoch,
                )

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

    def train_one_epoch(
        self,
        epoch: int,
        train_loader: object,
        train_losses: Dict[str, nn.Module],
        backward_loss: str,
    ) -> None:
        """
        Run one epoch: accumulate per-loss metrics, step the scheduler with the backward loss, then log.

        Parameters
        ----------
        epoch : int
            Epoch index passed to :meth:`print_train` and :meth:`log_train`.
        train_loader : object
            Iterable of ``(inputs, gts)`` batches; ``len(train_loader)`` normalizes the mean batch loss.
        train_losses : dict of str to torch.nn.Module
            Named loss modules used in :meth:`_train_one_batch`.
        backward_loss : str
            Key in ``train_losses`` whose output is back-propagated.

        Returns
        -------
        None
        """
        avg_losses = {name: 0.0 for name in train_losses}
        train_err = 0.0
        t0 = default_timer()
        self.n_samples = 0

        self.model.train()
        if self.pre_processor is not None:
            self.pre_processor.train()
        if self.post_processor is not None:
            self.post_processor.train()

        for sample in train_loader:
            loss, step_losses = self._train_one_batch(sample, train_losses, backward_loss)
            if self.scaler is not None:
                self.scaler.scale(loss).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                loss.backward()
                self.optimizer.step()

            train_err += step_losses[backward_loss]
            for name, val in step_losses.items():
                avg_losses[name] += val

        train_err /= len(train_loader)
        for name in avg_losses:
            avg_losses[name] /= self.n_samples

        if isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
            self.scheduler.step(train_err)
        elif self.scheduler is not None:
            self.scheduler.step()

        epoch_train_time = default_timer() - t0

        lr = None
        for pg in self.optimizer.param_groups:
            lr = pg["lr"]
        if self.verbose:
            self.print_train(epoch, epoch_train_time, avg_losses, train_err, lr)
        if self.save_logs:
            self.log_train(epoch, epoch_train_time, avg_losses, train_err, lr)

    def evaluate(
        self,
        eval_loaders: Dict[str, object],
        eval_losses: Optional[Union[nn.Module, Dict[str, nn.Module]]] = None,
        epoch: Optional[int] = None,
        eval_iter: Optional[Callable[..., Any]] = None,
    ) -> Dict[str, float]:
        """
        Compute mean per-sample losses per loader and metric, optionally save stacked last-batch outputs, and log.

        Parameters
        ----------
        eval_loaders : dict of str to object
            Loader names to iterables of ``(inputs, gts)`` batches.
        eval_losses : torch.nn.Module, dict of str to torch.nn.Module, or None, optional
            A single metric module, named metric modules, or None to skip metrics.
            A single module is wrapped as ``{"loss": module}``. Default is None.
        epoch : int or None, optional
            Epoch index for logging and for ``outputs_epoch_{epoch}.pt`` when ``save_outs``. Default is None.
        eval_iter : callable or None, optional
            If None, call ``self.model(**inputs)``; otherwise ``eval_iter(self.model, **inputs)``. Default is None.

        Returns
        -------
        eval_metrics : dict of str to float
            Keys ``f"{loader_name}_{loss_name}"`` mapping to mean loss per sample for that loader.
        """
        if isinstance(eval_losses, nn.Module):
            eval_losses = {"loss": eval_losses}

        self.model.eval()
        if self.pre_processor is not None:
            self.pre_processor.eval()
        if self.post_processor is not None:
            self.post_processor.eval()

        eval_metrics = {}
        if eval_losses is not None:
            for loader_name in eval_loaders.keys():
                for loss_name in eval_losses.keys():
                    eval_metrics[f"{loader_name}_{loss_name}"] = 0.0
        all_inputs = {}
        all_outs = {}
        all_gts = {}

        def _stack_batches(batch_list, n=None):
            combined = {}
            for k in batch_list[0]:
                vals = [b[k] for b in batch_list]
                if torch.is_tensor(vals[0]):
                    combined[k] = torch.cat(vals, dim=0) if n is None else torch.cat(vals, dim=0)[:n]
                else:
                    combined[k] = vals if n is None else vals[:n]
            return combined

        with torch.no_grad():
            for loader_name, eval_loader in eval_loaders.items():
                self.n_samples = 0
                batch_outs = []
                batch_inputs = []
                batch_gts = []
                for sample in eval_loader:
                    eval_step_losses, out, inp, gt = self._eval_one_batch(
                        sample,
                        eval_losses,
                        return_output=self.save_outs,
                        return_inputs=self.save_inputs,
                        return_gts=self.save_gts,
                        eval_iter=eval_iter,
                    )
                    if out is not None:
                        batch_outs.append(out)
                    if inp is not None:
                        batch_inputs.append(inp)
                    if gt is not None:
                        batch_gts.append(gt)
                    for loss_name, val_loss in eval_step_losses.items():
                        eval_metrics[f"{loader_name}_{loss_name}"] += val_loss
                for loss_name in eval_losses.keys():
                    eval_metrics[f"{loader_name}_{loss_name}"] /= self.n_samples
                if batch_outs:
                    all_outs[loader_name] = _stack_batches(batch_outs, self.n_outs)
                if batch_inputs:
                    all_inputs[loader_name] = _stack_batches(batch_inputs, self.n_outs)
                if batch_gts:
                    all_gts[loader_name] = _stack_batches(batch_gts, self.n_outs)

        if self.save_outs or self.save_inputs or self.save_gts:
            save_data = {}
            if self.save_inputs:
                save_data["inputs"] = all_inputs
            if self.save_outs:
                save_data["outputs"] = all_outs
            if self.save_gts:
                save_data["gts"] = all_gts
            self.save_dir.mkdir(parents=True, exist_ok=True)
            torch.save(save_data, self.save_dir / f"eval_epoch_{epoch}.pt")

        if eval_losses is not None:
            if self.verbose:
                self.print_eval(epoch, eval_metrics)
            if self.save_logs:
                self.log_eval(epoch, eval_metrics)
        return eval_metrics

    def _train_one_batch(
        self,
        sample: object,
        train_losses: Dict[str, nn.Module],
        backward_loss: str,
    ) -> Tuple[torch.Tensor, Dict[str, float]]:
        """
        Transfer a batch to ``device``, optionally run processors, forward the model, compute all losses,
        and return the backward-loss tensor together with all per-loss scalar values.

        Parameters
        ----------
        sample : object
            Pair ``(inputs, gts)`` of dicts; batch size is taken from dimension 0 of the first tensor in ``inputs``.
        train_losses : dict of str to torch.nn.Module
            Named loss modules ``loss(**outputs, **gts)``.
        backward_loss : str
            Key in ``train_losses`` whose tensor is returned for back-propagation.

        Returns
        -------
        loss : torch.Tensor
            Scalar tensor (shape ``()``) for ``backward`` in the training loop.
        step_losses : dict of str to float
            All loss values as Python floats for logging.
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
        batch_dim = int(first_tensor.shape[0])
        self.n_samples += batch_dim

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        if self.mixed_precision:
            with torch.autocast(device_type=self.autocast_device_type):
                outputs = self.model(**inputs)
                if self.post_processor is not None:
                    outputs = self.post_processor(outputs)
                loss_tensors = {
                    name: fn(**outputs, **gts) for name, fn in train_losses.items()
                }
        else:
            outputs = self.model(**inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            loss_tensors = {
                name: fn(**outputs, **gts) for name, fn in train_losses.items()
            }

        loss = loss_tensors[backward_loss]
        step_losses = {name: t.item() for name, t in loss_tensors.items()}
        return loss, step_losses

    def _eval_one_batch(
        self,
        sample: object,
        eval_losses: Dict[str, nn.Module],
        return_output: bool = False,
        return_inputs: bool = False,
        return_gts: bool = False,
        eval_iter: Optional[Callable[..., Any]] = None,
    ) -> Tuple[Dict[str, float], Optional[Dict[str, Any]], Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        """
        Evaluate one batch without gradients, record metric values, and optionally return CPU inputs/outputs/gts.

        Parameters
        ----------
        sample : object
            ``(inputs, gts)`` dicts with the same layout as training; batch size from dimension 0 of the first input tensor.
        eval_losses : dict of str to torch.nn.Module
            Metric names to scalar loss modules; must match keys used in :meth:`evaluate`.
        return_output : bool, optional
            If True, detach outputs to CPU in the second return value. Default is False.
        return_inputs : bool, optional
            If True, detach inputs to CPU in the third return value. Default is False.
        return_gts : bool, optional
            If True, detach gts to CPU in the fourth return value. Default is False.
        eval_iter : callable or None, optional
            If None, call ``self.model(**inputs)``; otherwise ``eval_iter(self.model, **inputs)``. Default is None.

        Returns
        -------
        eval_step_losses : dict of str to float
            Per-metric batch total as a Python float from ``.item()``.
        outputs : dict or None
            CPU-side postprocessed outputs if ``return_output`` is True; otherwise None.
        inputs : dict or None
            CPU-side inputs if ``return_inputs`` is True; otherwise None.
        gts : dict or None
            CPU-side ground truths if ``return_gts`` is True; otherwise None.
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
        batch_dim = int(first_tensor.shape[0])
        self.n_samples += batch_dim

        ret_inputs = None
        if return_inputs:
            ret_inputs = {k: (v.detach().cpu() if torch.is_tensor(v) else v) for k, v in inputs.items()}
        ret_gts = None
        if return_gts:
            ret_gts = {k: (v.detach().cpu() if torch.is_tensor(v) else v) for k, v in gts.items()}

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        # Forward and metrics; post-processor under autocast when enabled
        if self.mixed_precision:
            with torch.autocast(device_type=self.autocast_device_type):
                if eval_iter is None:
                    outputs = self.model(**inputs)
                else:
                    outputs = eval_iter(self.model, **inputs)
                if self.post_processor is not None:
                    outputs = self.post_processor(outputs)
                eval_step_losses = {}
                for loss_name, loss in eval_losses.items():
                    eval_step_losses[loss_name] = loss(**outputs, **gts).item()
        else:
            if eval_iter is None:
                outputs = self.model(**inputs)
            else:
                outputs = eval_iter(self.model, **inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            eval_step_losses = {
                loss_name: loss(**outputs, **gts).item()
                for loss_name, loss in eval_losses.items()
            }

        ret_outputs = None
        if return_output:
            ret_outputs = {k: (v.detach().cpu() if torch.is_tensor(v) else v) for k, v in outputs.items()}
        return eval_step_losses, ret_outputs, ret_inputs, ret_gts

    def print_train(
        self,
        epoch: int,
        epoch_time: float,
        avg_losses: Dict[str, float],
        train_err: float,
        lr: Optional[float] = None,
    ) -> None:
        """
        Print one training summary line and flush stdout.

        Parameters
        ----------
        epoch : int
            Epoch index in the leading bracket.
        epoch_time : float
            Wall-clock seconds spent in the epoch.
        avg_losses : dict of str to float
            Mean per-sample loss for each named training loss.
        train_err : float
            Mean of per-batch backward-loss values over batches (used by scheduler).
        lr : float or None, optional
            Last optimizer param-group learning rate, or None to print ``lr=N/A``. Default is None.

        Returns
        -------
        None
        """
        msg = f"[{epoch}] time={epoch_time:.2f}, "
        for name, val in avg_losses.items():
            msg += f"{name}={val:.4f}, "
        msg += f"train_err={train_err:.4f}, "
        msg += f"lr={lr:.3e}" if lr is not None else "lr=N/A"
        print(msg)
        sys.stdout.flush()

    def print_eval(
        self,
        epoch: Optional[int],
        eval_metrics: Dict[str, Any],
    ) -> None:
        """
        Print one evaluation line with metrics formatted to four decimals.

        Parameters
        ----------
        epoch : int or None
            Epoch index in the prefix; None is treated as 0 for display.
        eval_metrics : dict of str to float or torch.Tensor
            Metric name to float or scalar tensor; non-tensor non-float entries are skipped.

        Returns
        -------
        None
        """
        epoch = 0 if epoch is None else epoch
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
        epoch_time: float,
        avg_losses: Dict[str, float],
        train_err: float,
        lr: Optional[float] = None,
    ) -> None:
        """
        Append the same line as :meth:`print_train` to ``self.log_dir`` using UTF-8 and a trailing newline.

        Parameters
        ----------
        epoch : int
            Epoch index in the log line.
        epoch_time : float
            Wall-clock seconds for the epoch.
        avg_losses : dict of str to float
            Mean per-sample loss for each named training loss.
        train_err : float
            Mean per-batch backward-loss value for the epoch.
        lr : float or None, optional
            Learning rate formatted like :meth:`print_train`. Default is None.

        Returns
        -------
        None
        """
        msg = f"[{epoch}] time={epoch_time:.2f}, "
        for name, val in avg_losses.items():
            msg += f"{name}={val:.4f}, "
        msg += f"train_err={train_err:.4f}, "
        msg += f"lr={lr:.3e}" if lr is not None else "lr=N/A"
        with self.log_dir.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")

    def log_eval(
        self,
        epoch: Optional[int],
        eval_metrics: Dict[str, Any],
    ) -> None:
        """
        Append the same line as :meth:`print_eval` to ``self.log_dir`` using UTF-8 and a trailing newline.

        Parameters
        ----------
        epoch : int or None
            Epoch index in the prefix; None is treated as 0 for display.
        eval_metrics : dict of str to float or torch.Tensor
            Same structure as :meth:`print_eval`.

        Returns
        -------
        None
        """
        epoch = 0 if epoch is None else epoch
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
        optimizer: Optional[torch.optim.Optimizer] = None,
        scheduler: Optional[object] = None,
        scaler: Optional[torch.amp.GradScaler] = None,
        epoch: Optional[int] = None,
    ) -> None:
        """
        Save a checkpoint dict under ``self.save_dir`` for resuming training.

        Parameters
        ----------
        filename : str
            Base name without ``.pth``; the file is ``self.save_dir / f"{filename}.pth"``.
        model : torch.nn.Module
            Module whose ``state_dict`` is stored under ``"model"``.
        optimizer : torch.optim.Optimizer or None, optional
            If not None, store ``state_dict`` under ``"optimizer"``. Default is None.
        scheduler : object or None, optional
            If not None, store ``state_dict`` under ``"scheduler"``. Default is None.
        scaler : torch.amp.GradScaler or None, optional
            If not None, store AMP scaler state under ``"scaler"``. Default is None.
        epoch : int or None, optional
            If not None, store this integer under ``"epoch"``. Default is None.

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
