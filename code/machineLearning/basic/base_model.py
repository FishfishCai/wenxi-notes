import inspect
from typing import Any, Dict, Optional

import torch.nn as nn


class BaseModel(nn.Module):
    """Stores constructor metadata so checkpoints can rebuild the same model class."""

    def __init_subclass__(
        cls,
        name: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Set ``cls._name`` used in ``state_dict`` metadata for checkpoint reconstruction.

        Parameters
        ----------
        cls : type
            Subclass being registered.
        name : str or None, optional
            Stored name; if None, ``cls.__name__`` is used. Default is None.
        **kwargs : Any
            Forwarded to ``nn.Module.__init_subclass__``.

        Returns
        -------
        None
        """
        super().__init_subclass__(**kwargs)
        cls._name = name if name is not None else cls.__name__

    def __new__(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> "BaseModel":
        """
        Allocate an instance, record constructor arguments, and fill omitted keyword defaults from the signature.

        Parameters
        ----------
        cls : type
            Concrete ``BaseModel`` subclass to instantiate.
        *args : tuple
            Positional arguments passed to the subclass ``__init__``.
        **kwargs : dict
            Keyword arguments for ``__init__``; may include ``verbose`` to print signature diagnostics.

        Returns
        -------
        instance : BaseModel
            New instance with ``instance._init_kwargs`` storing full reconstruction metadata.
        """
        sig = inspect.signature(cls)
        model_name = cls.__name__

        verbose = kwargs.get("verbose", False)
        # Keys not present in the constructor signature
        for key in kwargs:
            if key not in sig.parameters:
                if verbose:
                    print(
                        f"Given argument key={key} "
                        f"that is not in {model_name}'s signature."
                    )

        # Defaults from the signature for missing kwargs
        for key, value in sig.parameters.items():
            if (value.default is not inspect._empty) and (key not in kwargs):
                if verbose:
                    print(
                        f"Keyword argument {key} not specified for model {model_name}, "
                        f"using default={value.default}."
                    )
                kwargs[key] = value.default

        kwargs["args"] = args
        kwargs["_name"] = cls._name
        ## ``nn.Module`` instance allocation and init metadata
        instance = super().__new__(cls)
        instance._init_kwargs = kwargs

        return instance

    def state_dict(
        self,
        destination: Optional[dict] = None,
        prefix: str = "",
        keep_vars: bool = False,
    ) -> Dict[str, Any]:
        """
        Return the module state dict and attach ``'_metadata'`` for ``BaseModel`` reconstruction.

        Parameters
        ----------
        destination : dict or None, optional
            Optional dict to fill; if None, a new dict is created. Default is None.
        prefix : str, optional
            Prefix for parameter and buffer names in keys. Default is ``""``.
        keep_vars : bool, optional
            If True, keep autograd history on tensors; if False, detach. Default is False.

        Returns
        -------
        state_dict : dict
            Mapping of names to tensors or buffers, plus ``'_metadata'`` copied from ``_init_kwargs``.
        """
        state_dict = super().state_dict(
            destination=destination,
            prefix=prefix,
            keep_vars=keep_vars,
        )
        state_dict["_metadata"] = self._init_kwargs
        return state_dict

    def load_state_dict(
        self,
        state_dict: Dict[str, Any],
        strict: bool = True,
        assign: bool = False,
    ) -> Any:
        """
        Load tensors into the module after removing ``'_metadata'`` from the checkpoint dict.

        Parameters
        ----------
        state_dict : dict
            Checkpoint mapping that may include ``'_metadata'`` alongside weights and buffers.
        strict : bool, optional
            If True, keys must match exactly. Default is True.
        assign : bool, optional
            If True, use direct assignment where supported. Default is False.

        Returns
        -------
        incompatible_keys : Any
            Return value of ``nn.Module.load_state_dict`` (missing and unexpected key reports).
        """
        state_dict.pop("_metadata", None)
        return super().load_state_dict(state_dict, strict=strict, assign=assign)
