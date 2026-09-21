import json
import sys
import torch
from accelerate import Accelerator
from accelerate.utils import set_seed
from itertools import chain, repeat
from pathlib import Path
from timeit import default_timer
from torch import nn
from torch.utils.data import DataLoader
from typing import Any, Callable, Dict, Iterable, Optional, Type, Union

from .baseModel import BaseModel
from .loss import Metric


StepFn = Callable[[nn.Module, Any], Dict[str, Any]]


def to_device(
    obj: Any,
    device: Any,
) -> Any:
    """
    Move every tensor inside a nested structure to a device, leaving other values untouched.

    Parameters
    ----------
    obj : Any
        Tensor, or an arbitrarily nested dict, list, or tuple that may contain tensors.
        Non-tensor leaves such as file paths or sample ids are returned as they are.
    device : Any
        Target device accepted by ``torch.Tensor.to``.

    Returns
    -------
    moved : Any
        New structure of the same shape with every tensor placed on ``device``.
    """
    if torch.is_tensor(obj):
        return obj.to(device, non_blocking=True)
    if isinstance(obj, dict):
        return {key: to_device(value, device) for key, value in obj.items()}
    if isinstance(obj, list):
        return [to_device(value, device) for value in obj]
    if isinstance(obj, tuple):
        return tuple(to_device(value, device) for value in obj)
    return obj


def scalar(
    value: Any,
) -> Any:
    """
    Convert tensor metric values into plain Python numbers.

    Parameters
    ----------
    value : Any
        Value returned by ``Metric.compute``, possibly a tensor or a mapping of tensors.

    Returns
    -------
    converted : Any
        Python number for a zero-dimensional tensor, nested list otherwise, mapping with
        every entry converted for a dict, and the original object for anything else.
    """
    if isinstance(value, torch.Tensor):
        return value.item() if value.ndim == 0 else value.tolist()
    if isinstance(value, dict):
        return {name: scalar(item) for name, item in value.items()}
    return value


class Trainer:
    """Step-based trainer that builds a model from a config or checkpoint and drives training and evaluation."""

    def __init__(
        self,
        *,
        model_class: Type[BaseModel],
        config_path: Union[str, Path],
        save_dir: Union[Path, str],
        optimizer: Optional[Callable[[nn.Module], torch.optim.Optimizer]] = None,
        scheduler: Optional[Callable[[torch.optim.Optimizer], object]] = None,
        accelerator: Optional[Accelerator] = None,
        grad_clip_norm: Optional[float] = None,
        seed: int = 0,
        deterministic: bool = False,
        compile_model: bool = False,
        verbose: bool = True,
        save_logs: bool = True,
    ) -> None:
        """
        Build the model, optimizer, and scheduler, restoring training state from a checkpoint.

        The file extension of ``config_path`` decides the mode: a ``.json`` file starts a
        fresh run from its hyper-parameters, a ``.pth`` checkpoint resumes model weights,
        optimizer, scheduler, step counter, and best metric value.

        Parameters
        ----------
        model_class : Type[BaseModel]
            Class used to build the model, which must subclass ``BaseModel``.
        config_path : Union[str, Path]
            Path to a ``.json`` hyper-parameter file or a ``.pth`` checkpoint.
        save_dir : Union[Path, str]
            Directory that receives checkpoints and ``logs.txt``.
        optimizer : Optional[Callable[[nn.Module], torch.optim.Optimizer]]
            Factory that builds the optimizer from the model. Training is unavailable when
            omitted, which is the evaluation-only mode. Default is None.
        scheduler : Optional[Callable[[torch.optim.Optimizer], object]]
            Factory that builds the learning-rate scheduler from the optimizer. It is
            stepped once per optimizer update. Default is None.
        accelerator : Optional[Accelerator]
            Accelerator carrying the device, mixed-precision, and gradient-accumulation
            settings. A default one is created when omitted. Default is None.
        grad_clip_norm : Optional[float]
            Maximum gradient norm applied before each optimizer update. No clipping when
            omitted. Default is None.
        seed : int
            Base seed for Python, NumPy, and torch. Each process is offset by its rank so
            that data augmentation differs across ranks. Default is 0.
        deterministic : bool
            Whether to request deterministic algorithms, which can slow training down.
            Default is False.
        compile_model : bool
            Whether to wrap the model with ``torch.compile``. Default is False.
        verbose : bool
            Whether the main process prints progress. Default is True.
        save_logs : bool
            Whether the main process appends log lines to ``logs.txt``. Default is True.
        """
        self.accelerator = accelerator if accelerator is not None else Accelerator()
        self.device = self.accelerator.device
        self._is_main = self.accelerator.is_main_process
        self.grad_clip_norm = grad_clip_norm
        set_seed(seed, device_specific=True, deterministic=deterministic)

        self.step = 0
        self.best_metric_value = float("inf")

        self.verbose = verbose and self._is_main
        self.save_logs = save_logs and self._is_main
        self.save_dir = Path(save_dir).expanduser().resolve()
        self.log_path = self.save_dir / "logs.txt"
        if self._is_main:
            self.save_dir.mkdir(parents=True, exist_ok=True)
        if self.save_logs:
            self.log_path.touch()

        # The optimizer factory needs the model, and resuming needs both before prepare
        # rewrites their keys, so this order is forced.
        ckpt = self._build_model(config_path, model_class)
        built_optimizer = optimizer(self.model) if optimizer is not None else None
        built_scheduler = (
            scheduler(built_optimizer)
            if (scheduler is not None and built_optimizer is not None)
            else None
        )
        if ckpt is not None:
            self._resume_state(ckpt, built_optimizer, built_scheduler)
        # Reseed from the resume point so continuing a run never replays past draws.
        set_seed(seed + self.step, device_specific=True, deterministic=deterministic)
        if compile_model:
            self.model = torch.compile(self.model)

        self.model = self.accelerator.prepare(self.model)
        self.optimizer = (
            self.accelerator.prepare(built_optimizer) if built_optimizer is not None else None
        )
        self.scheduler = (
            self.accelerator.prepare(built_scheduler) if built_scheduler is not None else None
        )

    def train_with_eval(
        self,
        *,
        max_steps: int,
        train_step: StepFn,
        train_loader: Iterable[Any],
        train_metrics: Optional[Dict[str, Metric]] = None,
        eval_step: Optional[Union[StepFn, Dict[str, StepFn]]] = None,
        eval_loaders: Optional[Dict[str, Iterable[Any]]] = None,
        eval_metrics: Optional[Dict[str, Dict[str, Metric]]] = None,
        log_interval: int = 100,
        eval_interval: int = 1000,
        save_interval: int = 1000,
    ) -> None:
        """
        Train until ``max_steps`` optimizer updates, logging, evaluating, and saving on schedule.

        A step counts one optimizer update, so gradient accumulation consumes several
        batches per step. The three intervals are independent, and each one also fires on
        the final step. ``best_model.pth`` tracks the first metric of the first evaluation
        loader, treating lower as better. Omitting the evaluation arguments trains only.

        Parameters
        ----------
        max_steps : int
            Global step at which training stops, counted from zero across resumes.
        train_step : StepFn
            Callable receiving the model and one batch and returning a dict that must hold
            a ``"loss"`` entry with a scalar tensor. The remaining entries are forwarded to
            ``train_metrics``.
        train_loader : Iterable[Any]
            Any iterable of batches. A finite one restarts automatically when exhausted.
        train_metrics : Optional[Dict[str, Metric]]
            Metrics recorded per logging window and reset afterwards. Default is None.
        eval_step : Optional[Union[StepFn, Dict[str, StepFn]]]
            Callable receiving the model and one batch and returning a dict forwarded to
            the metrics of that loader, or a mapping from loader name to such a callable.
            Required when ``eval_loaders`` is given. Default is None.
        eval_loaders : Optional[Dict[str, Iterable[Any]]]
            Named evaluation sets, each of which must be finite. Default is None.
        eval_metrics : Optional[Dict[str, Dict[str, Metric]]]
            Metrics per evaluation loader, keyed the same way as ``eval_loaders``.
            Default is None.
        log_interval : int
            Number of steps between log lines. Default is 100.
        eval_interval : int
            Number of steps between evaluations. Default is 1000.
        save_interval : int
            Number of steps between checkpoints. Default is 1000.
        """
        if self.optimizer is None:
            raise ValueError(
                "Training requires an optimizer; pass optimizer=... at construction."
            )
        train_metrics = train_metrics or {}
        eval_loaders = eval_loaders or {}
        eval_metrics = eval_metrics or {}

        for name, value in (
            ("max_steps", max_steps),
            ("log_interval", log_interval),
            ("eval_interval", eval_interval),
            ("save_interval", save_interval),
        ):
            if value < 1:
                raise ValueError(f"{name} must be positive, got {value}.")
        missing = sorted(set(eval_loaders) - set(eval_metrics))
        if missing:
            raise ValueError(
                f"eval_metrics has no entry for eval_loaders {missing}; it must be "
                "{loader_name: {metric_name: metric}}."
            )
        if eval_loaders and eval_step is None:
            raise ValueError("eval_loaders were given but eval_step is None.")

        message = (
            f"Training from step {self.step} to {max_steps} on {self.device}"
            f" (accumulate={self.accelerator.gradient_accumulation_steps},"
            f" processes={self.accelerator.num_processes})"
        )
        if eval_loaders:
            message += f", evaluating {sorted(eval_loaders)} every {eval_interval} steps"
        if self.verbose:
            print(message)
            sys.stdout.flush()

        if isinstance(train_loader, DataLoader):
            train_loader = self.accelerator.prepare(train_loader)
        batches = chain.from_iterable(repeat(train_loader))

        self.model.train()
        for metric in train_metrics.values():
            metric.reset()
        window_loss = 0.0
        window_batches = 0
        window_start = default_timer()

        while self.step < max_steps:
            with self.accelerator.accumulate(self.model):
                result = train_step(self.model, to_device(next(batches), self.device))
                loss = result.pop("loss")
                self.accelerator.backward(loss)
                if self.grad_clip_norm is not None and self.accelerator.sync_gradients:
                    self.accelerator.clip_grad_norm_(self.model.parameters(), self.grad_clip_norm)
                self.optimizer.step()
                if self.scheduler is not None:
                    self.scheduler.step()
                self.optimizer.zero_grad(set_to_none=True)
            for metric in train_metrics.values():
                metric.update(**result)
            window_loss = window_loss + loss.detach()
            window_batches += 1
            # Accumulation micro-batches are not optimizer updates, so they do not count.
            if not self.accelerator.sync_gradients:
                continue
            self.step += 1
            last = self.step >= max_steps

            if self.step % log_interval == 0 or last:
                train_loss = float(window_loss / window_batches)
                self._log({
                    "time": default_timer() - window_start,
                    "loss": train_loss,
                    "train": {n: scalar(m.compute()) for n, m in train_metrics.items()},
                    "lr": self.optimizer.param_groups[-1]["lr"],
                })
                for metric in train_metrics.values():
                    metric.reset()
                window_loss = 0.0
                window_batches = 0
                window_start = default_timer()

            if eval_loaders and (self.step % eval_interval == 0 or last):
                eval_results = self.evaluate(eval_loaders, eval_metrics, eval_step)
                self.model.train()
                first_results = eval_results[next(iter(eval_loaders))]
                if first_results:
                    value = next(iter(first_results.values()))
                    if value < self.best_metric_value:
                        self.best_metric_value = float(value)
                        self._save_state("best_model")

            if self.step % save_interval == 0 or last:
                self._save_state(f"step_{self.step}")

    def evaluate(
        self,
        eval_loaders: Dict[str, Iterable[Any]],
        eval_metrics: Dict[str, Dict[str, Metric]],
        eval_step: Union[StepFn, Dict[str, StepFn]],
    ) -> Dict[str, Dict[str, Any]]:
        """
        Run every evaluation loader to exhaustion and reduce its metrics.

        The model is switched to evaluation mode and gradients are disabled. Batch results
        are gathered across processes before reaching the metrics, so every rank computes
        the same value over the full data. This method also serves post-training
        evaluation on a trainer built from a checkpoint without an optimizer.

        Parameters
        ----------
        eval_loaders : Dict[str, Iterable[Any]]
            Named evaluation sets, each of which must be finite.
        eval_metrics : Dict[str, Dict[str, Metric]]
            Metrics per evaluation loader, keyed the same way as ``eval_loaders``.
        eval_step : Union[StepFn, Dict[str, StepFn]]
            Callable receiving the model and one batch and returning a dict forwarded to
            the metrics of that loader, or a mapping from loader name to such a callable.

        Returns
        -------
        eval_results : Dict[str, Dict[str, Any]]
            Mapping from loader name to its metric name and reduced value.
        """
        self.model.eval()
        eval_results: Dict[str, Dict[str, Any]] = {}

        with torch.no_grad():
            for loader_name, eval_loader in eval_loaders.items():
                step_fn = eval_step.get(loader_name) if isinstance(eval_step, dict) else eval_step
                if step_fn is None:
                    raise ValueError(f"eval_step has no entry for loader {loader_name!r}.")
                loader_metrics = eval_metrics[loader_name]
                for metric in loader_metrics.values():
                    metric.reset()
                if isinstance(eval_loader, DataLoader):
                    eval_loader = self.accelerator.prepare(eval_loader)
                for batch in eval_loader:
                    result = step_fn(self.model, to_device(batch, self.device))
                    result = self.accelerator.gather_for_metrics(result)
                    for metric in loader_metrics.values():
                        metric.update(**result)
                eval_results[loader_name] = {
                    name: scalar(metric.compute()) for name, metric in loader_metrics.items()
                }

        if eval_results:
            self._log(eval_results, prefix="Eval ")
        return eval_results

    def _build_model(
        self,
        config_path: Union[str, Path],
        model_class: Type[BaseModel],
    ) -> Optional[dict]:
        """
        Construct ``self.model`` from a JSON hyper-parameter file or a checkpoint.

        Both sources carry the same payload, a flat mapping passed to ``model_class`` as
        keyword arguments. A checkpoint also stores the model class path, which is checked
        against ``model_class`` before the model is built.

        Parameters
        ----------
        config_path : Union[str, Path]
            Path to a ``.json`` hyper-parameter file or a ``.pth`` checkpoint.
        model_class : Type[BaseModel]
            Class used to build the model, which must subclass ``BaseModel``.

        Returns
        -------
        ckpt : Optional[dict]
            Loaded checkpoint for a ``.pth`` source, None for a ``.json`` source.
        """
        path = Path(config_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Not found: {path}")

        suffix = path.suffix.lower()
        if suffix == ".json":
            config = json.loads(path.read_text(encoding="utf-8"))
            ckpt = None
        elif suffix == ".pth":
            ckpt = torch.load(path, map_location="cpu", weights_only=False)
            if "config" not in ckpt:
                raise KeyError('No "config" found in checkpoint; cannot reconstruct the model.')
            config = json.loads(ckpt["config"])
            saved_name = str(ckpt["model_class"]).rsplit(".", 1)[-1]
            if saved_name != model_class.__qualname__:
                raise ValueError(
                    f'Checkpoint holds model class "{saved_name}" but model_class is '
                    f'"{model_class.__qualname__}".'
                )
            if self.verbose:
                print(f'Loading config of model "{saved_name}" from checkpoint.')
                sys.stdout.flush()
        else:
            raise ValueError(f"Unsupported config file type: {suffix}")

        self.model = model_class(**config)
        if not isinstance(self.model, BaseModel):
            raise TypeError(
                f"{model_class.__qualname__} must subclass BaseModel so its "
                "config can be written to the checkpoint."
            )
        return ckpt

    def _resume_state(
        self,
        ckpt: dict,
        optimizer: Optional[torch.optim.Optimizer],
        scheduler: Optional[object],
    ) -> None:
        """
        Restore weights, training progress, and optimizer state from a checkpoint.

        Parameters
        ----------
        ckpt : dict
            Checkpoint returned by ``_build_model``.
        optimizer : Optional[torch.optim.Optimizer]
            Optimizer before ``Accelerator.prepare``, so its key names match the file.
        scheduler : Optional[object]
            Scheduler before ``Accelerator.prepare``, so its key names match the file.
        """
        self.model.load_state_dict(ckpt["model"])
        self.step = int(ckpt.get("step", 0))
        self.best_metric_value = float(ckpt.get("best_metric_value", float("inf")))
        for key, obj in (
            ("optimizer", optimizer),
            ("scheduler", scheduler),
            ("scaler", self.accelerator.scaler),
        ):
            if key in ckpt and obj is not None:
                obj.load_state_dict(ckpt[key])
        if self.verbose:
            print(f"Loaded checkpoint at step {self.step}.")
            sys.stdout.flush()

    def _save_state(
        self,
        filename: str,
    ) -> None:
        """
        Write weights, model config, and training state to ``<save_dir>/<filename>.pth``.

        All processes synchronise first and only the main one writes the file. The model
        is unwrapped from its distributed and compiled wrappers so the stored keys match a
        plain module.

        Parameters
        ----------
        filename : str
            File stem without extension, such as ``"best_model"`` or ``"step_1000"``.
        """
        self.accelerator.wait_for_everyone()
        if not self._is_main:
            return
        module = self.accelerator.unwrap_model(self.model, keep_torch_compile=False)
        ckpt = {
            "model": module.state_dict(),
            "config": json.dumps(module.config),
            "model_class": f"{type(module).__module__}.{type(module).__qualname__}",
            "step": int(self.step),
            "best_metric_value": self.best_metric_value,
        }
        for key, obj in (
            ("optimizer", self.optimizer),
            ("scheduler", self.scheduler),
            ("scaler", self.accelerator.scaler),
        ):
            if obj is not None:
                ckpt[key] = obj.state_dict()
        save_path = self.save_dir / f"{filename}.pth"
        torch.save(ckpt, save_path)
        if self.verbose:
            print(f"Saved training state to {save_path}")
            sys.stdout.flush()

    def _log(
        self,
        metrics: Dict[str, Any],
        prefix: str = "",
    ) -> None:
        """
        Format one line of metrics and send it to stdout and the log file.

        Nested mappings are flattened with ``/`` separators.

        Parameters
        ----------
        metrics : Dict[str, Any]
            Possibly nested mapping from name to value.
        prefix : str
            Text inserted before the step number in the line tag. Default is an empty string.
        """
        if not (self.verbose or self.save_logs):
            return

        def walk(
            values: Dict[str, Any],
            parent: str = "",
        ):
            """Yield flattened ``name=value`` fragments from a possibly nested mapping."""
            for name, value in values.items():
                full = f"{parent}/{name}" if parent else name
                if isinstance(value, dict):
                    yield from walk(value, full)
                elif isinstance(value, (int, float)):
                    yield f"{full}={value:.6f}"
                else:
                    yield f"{full}={value}"

        message = f"[{prefix}step {self.step}] " + ", ".join(walk(metrics))
        if self.verbose:
            print(message)
            sys.stdout.flush()
        if self.save_logs:
            with self.log_path.open("a", encoding="utf-8") as handle:
                handle.write(message + "\n")
