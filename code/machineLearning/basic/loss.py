import warnings
from typing import Any, Dict, Optional, Protocol, Union, runtime_checkable
import torch
from torch import nn


@runtime_checkable
class Metric(Protocol):
    """Stateful metric protocol with a reset / update / compute lifecycle."""

    def reset(self) -> None:
        """Clear accumulator state at the start of each loader pass."""
        ...

    def update(
        self,
        **kwargs: Any,
    ) -> Optional[torch.Tensor]:
        """Accumulate one batch and optionally return a scalar backward tensor.

        Parameters
        ----------
        **kwargs : Any
            Batched inputs required by the concrete metric (e.g. predictions
            and ground truths).

        Returns
        -------
        loss : Optional[torch.Tensor]
            Scalar tensor when the metric also produces a per-batch backward
            signal (i.e. it is a training loss); otherwise None.
        """
        ...

    def compute(self) -> Union[float, Dict[str, float]]:
        """Return the aggregated metric value after all updates.

        Returns
        -------
        value : Union[float, Dict[str, float]]
            Python float for single-valued metrics, or a `{sub_name: float}`
            dict when the metric reports several values at once.
        """
        ...


class LossMetric:
    """Adapter that turns a per-sample `nn.Module` loss into a mean-over-samples Metric."""

    def __init__(
        self,
        fn: nn.Module,
    ) -> None:
        """Wrap `fn` and initialise the running sum / sample counter.

        Parameters
        ----------
        fn : nn.Module
            Loss module expected to return a per-batch sum (not mean). If
            `fn.reduction == "mean"`, a warning is emitted because dividing
            a batch-mean by total sample count yields the mean of per-batch
            means, not the true sample mean.
        """
        if getattr(fn, "reduction", None) == "mean":
            warnings.warn(
                f"{fn.reduction=}. LossMetric divides by total samples and expects per-batch sum; "
                "with reduction='mean' the resulting metric will be the mean of per-batch means."
            )
        self.fn = fn
        self._sum = 0.0
        self._n = 0

    def reset(self) -> None:
        """Zero the running sum and sample counter."""
        self._sum = 0.0
        self._n = 0

    def update(
        self,
        **kwargs: Any,
    ) -> torch.Tensor:
        """Compute `fn(**kwargs)`, update running stats, and return the loss tensor.

        The batch size is inferred from the first tensor-valued kwarg.

        Parameters
        ----------
        **kwargs : Any
            Inputs forwarded to `self.fn`. Must contain at least one tensor
            so the batch size can be inferred from its leading dim.

        Returns
        -------
        loss : torch.Tensor
            Scalar tensor returned by `self.fn(**kwargs)`, suitable for
            `.backward()`.
        """
        loss = self.fn(**kwargs)
        # infer batch size from the first tensor kwarg
        bs = next((v.shape[0] for v in kwargs.values() if torch.is_tensor(v)), None)
        if bs is None:
            raise ValueError(
                "LossMetric.update needs at least one Tensor in kwargs to read batch size."
            )
        self._sum += float(loss.detach())
        self._n += int(bs)
        return loss

    def compute(self) -> float:
        """Return the running sum divided by total samples (at least 1)."""
        return self._sum / max(self._n, 1)
