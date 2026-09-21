import inspect
import torch.nn as nn
from typing import Any


class BaseModel(nn.Module):
    """Base class that records its resolved constructor arguments so a checkpoint can rebuild the model."""

    def __new__(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> "BaseModel":
        """
        Allocate an instance and store its fully resolved constructor arguments.

        The call is bound against the ``__init__`` signature resolved through the MRO, so
        positional and keyword arguments are normalised to parameter names and omitted
        parameters are filled from their defaults. Rebuilding an equivalent model is
        therefore always ``cls(**instance.config)``, whatever call style was used here.

        Parameters
        ----------
        cls : type
            Concrete ``BaseModel`` subclass to instantiate.
        *args : Any
            Positional arguments forwarded to the subclass ``__init__``.
        **kwargs : Any
            Keyword arguments forwarded to the subclass ``__init__``.

        Returns
        -------
        instance : BaseModel
            New instance whose ``config`` attribute holds the resolved
            ``{parameter_name: value}`` mapping.
        """
        sig = inspect.signature(cls.__init__)
        self_param, *parameters = sig.parameters.values()
        for param in parameters:
            if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
                raise TypeError(
                    f"{cls.__name__}.__init__ declares *{param.name} or **{param.name}; "
                    "an explicit signature is required to rebuild it from a checkpoint."
                )
        bound = sig.bind(cls, *args, **kwargs)
        bound.apply_defaults()

        instance = super().__new__(cls)
        instance.config = {
            name: value
            for name, value in bound.arguments.items()
            if name != self_param.name
        }
        return instance
