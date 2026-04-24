import json
import sys
from pathlib import Path
from timeit import default_timer
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union
import torch
from torch import nn

from .base_model import BaseModel
from .loss import Metric


class Trainer:
    """Model trainer with AMP, checkpointing, scheduling, and pluggable metrics."""

    def __init__(
        self,
        *,
        model_class: Type[BaseModel],
        optimizer: Optional[Callable[[nn.Module], torch.optim.Optimizer]] = None,
        scheduler: Optional[Callable[[torch.optim.Optimizer], object]] = None,
        pre_processor: Optional[nn.Module] = None,
        post_processor: Optional[nn.Module] = None,
        config_path: Union[str, Path],
        save_dir: Union[Path, str],
        resume: bool = True,
        device: str,
        mixed_precision: bool = False,
        compile_model: bool = True,
        verbose: bool = True,
        save_logs: bool = True,
        save_outs: bool = False,
        save_inps: bool = False,
        save_gts: bool = False,
    ) -> None:
        """Construct a Trainer from a model class and a config/checkpoint path.

        The model is built from `config_path` (JSON config or `.pth` checkpoint).
        If `resume` is True and a checkpoint was loaded, optimizer/scheduler/
        scaler and epoch counter are restored.

        Parameters
        ----------
        model_class : Type[BaseModel]
            Class used to build the model from loaded init args/kwargs.
        optimizer : Optional[Callable[[nn.Module], torch.optim.Optimizer]]
            Factory that builds an optimizer from the model. Default None;
            training is disabled unless provided.
        scheduler : Optional[Callable[[torch.optim.Optimizer], object]]
            Factory that builds a scheduler from the optimizer. Default None.
        pre_processor : Optional[nn.Module]
            Module applied to (inputs, gts) before the model. Default None.
        post_processor : Optional[nn.Module]
            Module applied to model outputs before metric update. Default None.
        config_path : Union[str, Path]
            Path to a `.json` model config or a `.pth` checkpoint.
        save_dir : Union[Path, str]
            Directory for checkpoints, logs, and eval dumps.
        resume : bool
            Restore optimizer/scheduler/scaler/epoch from checkpoint if
            available. Default True.
        device : str
            Torch device string (e.g. "cuda", "cuda:0", "cpu").
        mixed_precision : bool
            Enable AMP; only effective when device is CUDA. Default False.
        compile_model : bool
            Run `torch.compile` on the model after load. Default True.
        verbose : bool
            Print progress and log messages. Default True.
        save_logs : bool
            Append epoch logs to `<save_dir>/logs.txt`. Default True.
        save_outs : bool
            Collect model outputs during eval and dump to `eval.pt`.
            Default False.
        save_inps : bool
            Collect inputs during eval and dump to `eval.pt`. Default False.
        save_gts : bool
            Collect ground truths during eval and dump to `eval.pt`.
            Default False.
        """
        self.model_class = model_class
        self.device = device

        self.pre_processor = pre_processor
        self.post_processor = post_processor
        if self.pre_processor is not None:
            self.pre_processor.to(self.device)
        if self.post_processor is not None:
            self.post_processor.to(self.device)

        # AMP only on CUDA
        use_amp = mixed_precision and "cuda" in self.device
        self.mixed_precision = use_amp
        self.autocast_device_type = "cuda" if "cuda" in self.device else "cpu"
        self.scaler = torch.amp.GradScaler() if use_amp else None

        self.epoch = 0

        self.verbose = verbose
        self.save_dir = Path(save_dir).expanduser().resolve()
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.save_logs = save_logs
        if self.save_logs:
            self.log_path = self.save_dir / "logs.txt"
            self.log_path.touch()
        self.save_outs = save_outs
        self.save_inps = save_inps
        self.save_gts = save_gts

        # build model from config/checkpoint, then optionally resume state
        ckpt = self._load_config(config_path)
        self.optimizer = optimizer(self.model) if optimizer is not None else None
        self.scheduler = (
            scheduler(self.optimizer)
            if (scheduler is not None and self.optimizer is not None)
            else None
        )
        if resume and ckpt is not None:
            self._resume_state(ckpt)
        if compile_model:
            self.model = torch.compile(self.model)

    def train_with_eval(
        self,
        *,
        n_epochs: int,
        eval_interval: int = 1,
        save_interval: int = 50,
        train_loader: object,
        eval_loaders: Optional[Dict[str, object]] = None,
        train_metrics: Dict[str, Metric],
        eval_metrics: Optional[Union[Dict[str, Metric], Dict[str, Dict[str, Metric]]]] = None,
        train_iter: Optional[Callable[..., Any]] = None,
        eval_iter: Optional[Union[Callable[..., Any], Dict[str, Callable[..., Any]]]] = None,
    ) -> None:
        """Run the train/eval loop up to `n_epochs`, saving best and periodic checkpoints.

        Evaluates every `eval_interval` epochs and saves `best_model.pth` when
        the first metric of the first eval loader improves (lower is better).
        Saves `epoch_<i>.pth` every `save_interval` epochs.

        Parameters
        ----------
        n_epochs : int
            Target epoch count. Training resumes from `self.epoch`.
        eval_interval : int
            Run eval every N epochs. Default 1.
        save_interval : int
            Save a periodic checkpoint every N epochs. Default 50.
        train_loader : object
            Iterable yielding (inputs, gts) batches for training.
        eval_loaders : Optional[Dict[str, object]]
            Named eval iterables. Default None (no eval).
        train_metrics : Dict[str, Metric]
            Metrics computed per training epoch. The first one produces the
            backward tensor.
        eval_metrics : Optional[Union[Dict[str, Metric], Dict[str, Dict[str, Metric]]]]
            Metrics computed per eval loader. A flat `{metric_name: Metric}`
            dict is shared across all loaders; a nested
            `{loader_name: {metric_name: Metric}}` dict assigns a distinct set
            per loader. Required if `eval_loaders` is set.
        train_iter : Optional[Callable[..., Any]]
            Custom forward wrapper for training. Default None (uses
            `model(**inputs)`).
        eval_iter : Optional[Union[Callable[..., Any], Dict[str, Callable[..., Any]]]]
            Custom forward wrapper for eval. A single callable is used for all
            loaders; a dict maps `loader_name -> callable` for per-loader
            dispatch. Default None.
        """
        eval_loaders = eval_loaders or {}
        eval_metrics = eval_metrics or {}
        if eval_loaders and not eval_metrics:
            raise ValueError(
                "eval_loaders is non-empty but eval_metrics is empty; "
                "provide at least one evaluation metric, or use an empty eval_loaders."
            )
        if self.verbose:
            parts = [f"Training on {len(train_loader.dataset)} samples"]
            if eval_loaders:
                eval_parts = ", ".join(
                    f"{k}={len(v.dataset)} samples" for k, v in eval_loaders.items()
                )
                parts.append(f"evaluating on {len(eval_loaders)} loaders: {eval_parts}")
            print(", ".join(parts))
            sys.stdout.flush()

        best_metric_value = float("inf")

        # main training loop
        while self.epoch < n_epochs:
            self.train(train_loader, train_metrics, train_iter)
            if (self.epoch + 1) % eval_interval == 0 and eval_loaders:
                eval_results = self.evaluate(eval_loaders, eval_metrics, eval_iter)
                # pick first metric of first loader as the "best" signal
                first_loader_results = eval_results[next(iter(eval_loaders))]
                if first_loader_results:
                    val = next(iter(first_loader_results.values()))
                    if isinstance(val, (int, float)) and val < best_metric_value:
                        best_metric_value = val
                        self._save_state("best_model")
            if (self.epoch + 1) % save_interval == 0:
                self._save_state(f"epoch_{self.epoch}")
            self.epoch += 1

    def train(
        self,
        train_loader: object,
        train_metrics: Dict[str, Metric],
        train_iter: Optional[Callable[..., Any]] = None,
    ) -> None:
        """Run one training epoch over `train_loader`.

        The first metric in `train_metrics` produces the backward tensor. The
        scheduler is stepped at the end of the epoch; `ReduceLROnPlateau` uses
        the scalar value of that first metric.

        Parameters
        ----------
        train_loader : object
            Iterable yielding (inputs, gts) batches.
        train_metrics : Dict[str, Metric]
            Metrics updated per batch. Iteration order matters: the first
            yields the backward tensor.
        train_iter : Optional[Callable[..., Any]]
            Custom forward wrapper receiving the model and unpacked inputs.
            Default None (uses `model(**inputs)`).
        """
        if self.optimizer is None:
            raise ValueError(
                "Trainer.train() requires an optimizer; pass optimizer=... at construction."
            )
        self._set_mode(training=True)
        backward_metric = next(iter(train_metrics))

        for m in train_metrics.values():
            m.reset()
        t0 = default_timer()

        # one step per batch
        for sample in train_loader:
            backward_tensor = self._train_one_batch(sample, train_metrics, train_iter)
            if self.scaler is not None:
                self.scaler.scale(backward_tensor).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                backward_tensor.backward()
                self.optimizer.step()

        metric_values = {name: m.compute() for name, m in train_metrics.items()}

        # scheduler step (plateau uses backward metric value)
        if isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
            backward_val = metric_values[backward_metric]
            if not isinstance(backward_val, (int, float)):
                raise TypeError(
                    f"ReduceLROnPlateau requires a scalar from first train_metric.compute(), "
                    f"got {type(backward_val).__name__}."
                )
            self.scheduler.step(backward_val)
        elif self.scheduler is not None:
            self.scheduler.step()

        epoch_train_time = default_timer() - t0
        lr = self.optimizer.param_groups[-1]["lr"]
        self._log({"time": epoch_train_time, "train": metric_values, "lr": lr})

    def evaluate(
        self,
        eval_loaders: Dict[str, object],
        eval_metrics: Optional[Union[Dict[str, Metric], Dict[str, Dict[str, Metric]]]] = None,
        eval_iter: Optional[Union[Callable[..., Any], Dict[str, Callable[..., Any]]]] = None,
    ) -> Dict[str, Dict[str, Any]]:
        """Run eval over every named loader and return the aggregated metric values.

        When any of `save_inps`/`save_outs`/`save_gts` is set, stacks the
        corresponding tensors across batches and dumps them to `eval.pt`.

        Parameters
        ----------
        eval_loaders : Dict[str, object]
            Named iterables yielding (inputs, gts) batches.
        eval_metrics : Optional[Union[Dict[str, Metric], Dict[str, Dict[str, Metric]]]]
            Metrics computed per loader. A flat `{metric_name: Metric}` dict
            is shared across all loaders; a nested
            `{loader_name: {metric_name: Metric}}` dict assigns a distinct set
            per loader. Default None (no metric computation).
        eval_iter : Optional[Union[Callable[..., Any], Dict[str, Callable[..., Any]]]]
            Custom forward wrapper. A single callable is shared across all
            loaders; a dict maps `loader_name -> callable` so each loader uses
            its own iterator. Default None (uses `model(**inputs)`).

        Returns
        -------
        eval_results : Dict[str, Dict[str, Any]]
            Mapping `loader_name -> {metric_name -> metric_value}`.
        """
        self._set_mode(training=False)
        eval_metrics = eval_metrics or {}
        # detect nested per-loader layout by inspecting the first value
        per_loader_metrics = bool(eval_metrics) and isinstance(
            next(iter(eval_metrics.values())), dict
        )

        eval_results: Dict[str, Dict[str, Any]] = {}
        save_spec = [
            ("inputs", self.save_inps, {}),
            ("outputs", self.save_outs, {}),
            ("gts", self.save_gts, {}),
        ]

        with torch.no_grad():
            for loader_name, eval_loader in eval_loaders.items():
                # dispatch per-loader iter / metrics when a dict is passed
                loader_iter = eval_iter.get(loader_name) if isinstance(eval_iter, dict) else eval_iter
                loader_metrics = eval_metrics.get(loader_name, {}) if per_loader_metrics else eval_metrics
                for m in loader_metrics.values():
                    m.reset()
                batches = {name: [] for name, _, _ in save_spec}
                for sample in eval_loader:
                    out, inp, gt = self._eval_one_batch(sample, loader_metrics, loader_iter)
                    for name, val in (("inputs", inp), ("outputs", out), ("gts", gt)):
                        if val is not None:
                            batches[name].append(val)
                eval_results[loader_name] = {
                    name: m.compute() for name, m in loader_metrics.items()
                }
                for name, _, target in save_spec:
                    if batches[name]:
                        target[loader_name] = self._stack_batches(batches[name])

        # dump requested payloads to a single eval.pt file
        save_data = {name: target for name, flag, target in save_spec if flag}
        if save_data:
            torch.save(save_data, self.save_dir / "eval.pt")

        if eval_metrics:
            self._log(eval_results, prefix="Eval ")
        return eval_results

    def _to_device(
        self,
        d: Dict[str, Any],
    ) -> None:
        """Move every torch tensor value of `d` to `self.device` in-place.

        Parameters
        ----------
        d : Dict[str, Any]
            Dict whose tensor values are moved in-place; non-tensor values
            are left untouched.
        """
        for k, v in d.items():
            if torch.is_tensor(v):
                d[k] = v.to(self.device, non_blocking=True)

    @staticmethod
    def _to_cpu(
        d: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Return a copy of `d` with every tensor value detached on CPU."""
        return {k: (v.detach().cpu() if torch.is_tensor(v) else v) for k, v in d.items()}

    def _set_mode(
        self,
        training: bool,
    ) -> None:
        """Set model, pre-processor, and post-processor to `train()` or `eval()` mode.

        Parameters
        ----------
        training : bool
            True for `train()`, False for `eval()`.
        """
        mode = "train" if training else "eval"
        for m in (self.model, self.pre_processor, self.post_processor):
            if m is not None:
                getattr(m, mode)()

    @staticmethod
    def _stack_batches(
        batch_list: list,
    ) -> Dict[str, Any]:
        """Concatenate a list of batch dicts along dim 0 for tensors, else list them.

        Parameters
        ----------
        batch_list : list
            Non-empty list of dicts sharing identical keys. Each value is
            either a torch tensor or an arbitrary Python object.

        Returns
        -------
        combined : Dict[str, Any]
            Dict with the same keys; tensor values concatenated along dim 0,
            non-tensor values kept as lists in batch order.
        """
        combined = {}
        for k in batch_list[0]:
            vals = [b[k] for b in batch_list]
            if torch.is_tensor(vals[0]):
                combined[k] = torch.cat(vals, dim=0)
            else:
                combined[k] = vals
        return combined

    def _train_one_batch(
        self,
        sample: object,
        train_metrics: Dict[str, Metric],
        train_iter: Optional[Callable[..., Any]] = None,
    ) -> torch.Tensor:
        """Run one training batch: forward, metric update, and return the backward tensor.

        The first metric in `train_metrics` must return a Tensor from its
        `update()` call; that Tensor is returned as the backward target.

        Parameters
        ----------
        sample : object
            Pair `(inputs, gts)` where each half is a dict of tensors.
        train_metrics : Dict[str, Metric]
            Metrics updated with `(outputs, gts)`. Iteration order matters.
        train_iter : Optional[Callable[..., Any]]
            Custom forward wrapper. Default None (uses `model(**inputs)`).

        Returns
        -------
        backward_tensor : torch.Tensor
            Scalar tensor produced by the first metric's `update()`; used for
            backward.
        """
        self.optimizer.zero_grad(set_to_none=True)

        inputs, gts = sample
        self._to_device(inputs)
        self._to_device(gts)

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        # forward + metric update under autocast
        with torch.autocast(
            device_type=self.autocast_device_type,
            enabled=self.mixed_precision,
        ):
            outputs = self.model(**inputs) if train_iter is None else train_iter(self.model, **inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            # first metric yields backward tensor; remaining metrics only update
            metrics_iter = iter(train_metrics.values())
            backward_tensor = next(metrics_iter).update(**outputs, **gts)
            for m in metrics_iter:
                m.update(**outputs, **gts)

        if not isinstance(backward_tensor, torch.Tensor):
            raise RuntimeError(
                f"first train_metric.update() must return a Tensor for backward, "
                f"got {type(backward_tensor).__name__}."
            )
        return backward_tensor

    def _eval_one_batch(
        self,
        sample: object,
        eval_metrics: Dict[str, Metric],
        eval_iter: Optional[Callable[..., Any]] = None,
    ) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        """Run one eval batch: forward, metric update, and return CPU-detached payloads.

        Returned payloads are gated by the `save_inps`/`save_outs`/`save_gts`
        flags; unselected slots are returned as None.

        Parameters
        ----------
        sample : object
            Pair `(inputs, gts)` where each half is a dict of tensors.
        eval_metrics : Dict[str, Metric]
            Metrics updated with `(outputs, gts)`.
        eval_iter : Optional[Callable[..., Any]]
            Custom forward wrapper. Default None (uses `model(**inputs)`).

        Returns
        -------
        outputs : Optional[Dict[str, Any]]
            Model outputs detached on CPU if `save_outs` else None.
        inputs : Optional[Dict[str, Any]]
            Pre-processor inputs detached on CPU if `save_inps` else None.
        gts : Optional[Dict[str, Any]]
            Ground truths detached on CPU if `save_gts` else None.
        """
        inputs, gts = sample
        self._to_device(inputs)
        self._to_device(gts)

        # snapshot raw inputs/gts before pre_processor mutates them
        ret_inputs = self._to_cpu(inputs) if self.save_inps else None
        ret_gts = self._to_cpu(gts) if self.save_gts else None

        if self.pre_processor is not None:
            inputs, gts = self.pre_processor(inputs, gts)

        with torch.autocast(
            device_type=self.autocast_device_type,
            enabled=self.mixed_precision,
        ):
            outputs = self.model(**inputs) if eval_iter is None else eval_iter(self.model, **inputs)
            if self.post_processor is not None:
                outputs = self.post_processor(outputs)
            for m in eval_metrics.values():
                m.update(**outputs, **gts)

        ret_outputs = self._to_cpu(outputs) if self.save_outs else None
        return ret_outputs, ret_inputs, ret_gts

    def _load_config(
        self,
        config_path: Union[str, Path],
    ) -> Optional[dict]:
        """Build `self.model` from a JSON config or a `.pth` checkpoint.

        For `.json`, the root must be a dict; its optional `args` key provides
        positional init args and the remaining keys provide kwargs. For `.pth`,
        the checkpoint is `{"model": state_dict_with_metadata, ...}` and init
        args/kwargs come from `state_dict["_metadata"]`.

        Parameters
        ----------
        config_path : Union[str, Path]
            Path to a `.json` config or a `.pth` checkpoint.

        Returns
        -------
        ckpt : Optional[dict]
            Loaded checkpoint dict for `.pth`; None for `.json`.
        """
        path = Path(config_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Not found: {path}")

        suffix = path.suffix.lower()
        if suffix == ".json":
            cfg = json.loads(path.read_text(encoding="utf-8")) or {}
            if not isinstance(cfg, dict):
                raise TypeError(f"JSON root must be a dict, got {type(cfg)}")
            init_args = cfg.pop("args", []) or []
            init_kwargs = cfg
            ckpt = None
        elif suffix == ".pth":
            ckpt = torch.load(path, map_location=self.device, weights_only=False)
            if not isinstance(ckpt, dict) or not isinstance(ckpt.get("model"), dict):
                raise KeyError(
                    'Checkpoint must be a dict with a dict field "model" (model.state_dict()).'
                )
            # recover init args/kwargs from state_dict metadata
            init_meta = ckpt["model"].get("_metadata")
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
            init_kwargs = {k: v for k, v in init_meta.items() if k not in ("_name", "args")}
        else:
            raise ValueError(f"Unsupported config file type: {suffix}")

        if not isinstance(init_args, (list, tuple)):
            raise TypeError(f"'args' must be a list/tuple, got {type(init_args)}")
        init_kwargs["mixed_precision"] = self.mixed_precision
        self.model = self.model_class(*init_args, **init_kwargs).to(self.device)
        return ckpt

    def _resume_state(
        self,
        ckpt: dict,
    ) -> None:
        """Restore model weights plus optional scaler/optimizer/scheduler state from `ckpt`.

        Also advances `self.epoch` to `ckpt["epoch"] + 1` when present.

        Parameters
        ----------
        ckpt : dict
            Checkpoint loaded by `_load_config` from a `.pth` file. Expected
            keys: `"model"` (state dict), optional `"epoch"`, `"scaler"`,
            `"optimizer"`, `"scheduler"`.
        """
        self.model.load_state_dict(ckpt["model"])
        if "epoch" in ckpt:
            self.epoch = int(ckpt["epoch"]) + 1
            if self.verbose:
                print(f"Loading checkpoint from epoch {self.epoch - 1}.")
                sys.stdout.flush()
        for k, v in (
            ("scaler", self.scaler),
            ("optimizer", self.optimizer),
            ("scheduler", self.scheduler),
        ):
            if k in ckpt and v is not None:
                v.load_state_dict(ckpt[k])

    def _save_state(
        self,
        filename: str,
    ) -> None:
        """Save model state plus optional scaler/optimizer/scheduler to `<save_dir>/<filename>.pth`.

        Handles `torch.compile` models by saving the underlying `_orig_mod`.

        Parameters
        ----------
        filename : str
            File stem (no extension); `.pth` is appended.
        """
        save_path = self.save_dir / f"{filename}.pth"
        # unwrap torch.compile wrapper if present
        mod = self.model._orig_mod if hasattr(self.model, "_orig_mod") else self.model
        ckpt = {"model": mod.state_dict(), "epoch": int(self.epoch)}
        for k, v in (
            ("scaler", self.scaler),
            ("optimizer", self.optimizer),
            ("scheduler", self.scheduler),
        ):
            if v is not None:
                ckpt[k] = v.state_dict()
        torch.save(ckpt, save_path)
        if self.verbose:
            print(f"Saved training state to {save_path}")
            sys.stdout.flush()

    def _log(
        self,
        metrics: Dict[str, Any],
        prefix: str = "",
    ) -> None:
        """Format `metrics` as `key=value` pairs and print and/or append to the log file.

        Nested dicts are flattened with `/` separators. Tensors are converted
        via `.item()`; None values become `N/A`; non-numeric leaves are skipped.

        Parameters
        ----------
        metrics : Dict[str, Any]
            Possibly nested dict of scalar / tensor / None values.
        prefix : str
            Prefix written inside the `[...]` tag before the epoch number.
            Default "".
        """
        def walk(
            d: Dict[str, Any],
            parent: str = "",
        ):
            """Yield `key=value` strings, flattening nested dicts with `/` separators."""
            for name, val in d.items():
                full = f"{parent}/{name}" if parent else name
                if isinstance(val, dict):
                    yield from walk(val, full)
                    continue
                if isinstance(val, torch.Tensor):
                    val = float(val.item())
                if val is None:
                    yield f"{full}=N/A"
                elif isinstance(val, (int, float)):
                    yield f"{full}={val:.4f}"

        msg = f"[{prefix}{self.epoch}] " + ", ".join(walk(metrics))
        if self.verbose:
            print(msg)
            sys.stdout.flush()
        if self.save_logs:
            with self.log_path.open("a", encoding="utf-8") as f:
                f.write(msg + "\n")
