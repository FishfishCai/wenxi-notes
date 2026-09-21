import torch
from typing import Any, Dict, Protocol, Union, runtime_checkable


@runtime_checkable
class Metric(Protocol):
    """Protocol for a stateful metric that accumulates over batches and reduces once per pass."""

    def reset(self) -> None:
        """Clear the accumulated state before a new pass."""
        ...

    def update(
        self,
        **kwargs: Any,
    ) -> None:
        """
        Accumulate the contribution of one batch.

        Parameters
        ----------
        **kwargs : Any
            Entries of the dict returned by the step function, with ``"loss"`` removed.
            Parameter names must match the keys the step function produces.
        """
        ...

    def compute(self) -> Union[torch.Tensor, float, Dict[str, float]]:
        """
        Reduce the accumulated state into the metric value.

        Returns
        -------
        value : Union[torch.Tensor, float, Dict[str, float]]
            Scalar value, or a mapping when the metric reports several numbers at once.
        """
        ...
