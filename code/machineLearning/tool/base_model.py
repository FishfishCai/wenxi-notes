import inspect
import torch.nn as nn


class BaseModel(nn.Module):
    """Base class that stores initialization metadata for checkpoint reconstruction."""

    def __init_subclass__(cls, name=None, **kwargs):
        """
        Set ``cls._name`` for checkpoint metadata (used in ``_metadata`` when saving state_dict).

        Parameters
        ----------
        cls : type
            Subclass being created.
        name : str or None, optional
            Display name for the subclass; if None, the class name is used.
        **kwargs : dict
            Additional keyword arguments forwarded to ``nn.Module.__init_subclass__``.
        """
        super().__init_subclass__(**kwargs)
        cls._name = name if name is not None else cls.__name__

    def __new__(cls, *args, **kwargs):
        """
        Allocate an instance and capture full init arguments; fill missing kwargs from the class signature.
        Optionally print signature-mismatch messages when ``verbose`` is True in ``kwargs``.

        Parameters
        ----------
        cls : type
            Class to instantiate (subclass of BaseModel).
        *args : tuple
            Positional arguments for the class constructor.
        **kwargs : dict
            Keyword arguments for the class constructor; may include ``verbose`` for diagnostics.

        Returns
        -------
        instance : BaseModel
            New instance with ``instance._init_kwargs`` holding full init metadata for reconstruction.
        """
        sig = inspect.signature(cls)
        model_name = cls.__name__

        verbose = kwargs.get("verbose", False)
        # Warn on keys not in constructor signature
        for key in kwargs:
            if key not in sig.parameters:
                if verbose:
                    print(
                        f"Given argument key={key} "
                        f"that is not in {model_name}'s signature."
                    )

        # Fill missing kwargs from signature defaults
        for key, value in sig.parameters.items():
            if (value.default is not inspect._empty) and (key not in kwargs):
                if verbose:
                    print(
                        f"Keyword argument {key} not specified for model {model_name}, "
                        f"using default={value.default}."
                    )
                kwargs[key] = value.default

        # Attach full init metadata for checkpoint reconstruction
        kwargs["args"] = args
        kwargs["_name"] = cls._name
        ## Allocate instance and attach init metadata
        instance = super().__new__(cls)
        instance._init_kwargs = kwargs

        return instance

    def state_dict(self, destination: dict=None, prefix: str='', keep_vars: bool=False):
        """
        Return module state dict and attach init metadata under the ``'_metadata'`` key.

        Parameters
        ----------
        destination : dict or None, optional
            If provided, dict to populate with state; otherwise a new dict is created.
        prefix : str, optional
            Prefix prepended to parameter and buffer names in the returned dict.
        keep_vars : bool, optional
            If True, keep tensor values in the computation graph; default False detaches.

        Returns
        -------
        state_dict : dict
            Parameter/buffer name -> tensor mapping, plus ``'_metadata'`` with ``_init_kwargs``.
        """
        state_dict = super().state_dict(destination=destination, prefix=prefix, keep_vars=keep_vars)
        state_dict['_metadata'] = self._init_kwargs
        return state_dict

    def load_state_dict(self, state_dict, strict=True, assign=False):
        """
        Load parameters and buffers from a state dict; strip ``'_metadata'`` before delegating to ``nn.Module``.

        Parameters
        ----------
        state_dict : dict
            State dict with parameter/buffer tensors and optionally ``'_metadata'``.
        strict : bool, optional
            If True, require exact key match between state_dict and module.
        assign : bool, optional
            If True, use in-place assignment where supported by ``nn.Module.load_state_dict``.

        Returns
        -------
        result : object
            Return value from ``nn.Module.load_state_dict`` (e.g., missing/unexpected keys).
        """
        state_dict.pop("_metadata", None)
        return super().load_state_dict(state_dict, strict=strict, assign=assign)
    