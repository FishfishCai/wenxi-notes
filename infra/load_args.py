import json
from pathlib import Path
from types import SimpleNamespace
from typing import Union


def load_args(
    config_path: Union[str, Path],
) -> SimpleNamespace:
    """
    Read a JSON experiment configuration into an attribute-access namespace.

    One file describes one experiment. Every top-level key becomes an attribute, so keys
    must be valid Python identifiers.

    Parameters
    ----------
    config_path : Union[str, Path]
        Path to a ``.json`` file whose root is a JSON object.

    Returns
    -------
    args : SimpleNamespace
        Namespace holding one attribute per top-level key of the file.
    """
    path = Path(config_path).expanduser()
    if path.suffix.lower() != ".json":
        raise ValueError(f"config_path must be a .json file, got: {path}")

    config = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise TypeError(
            f"Config root must be a JSON object, got {type(config).__name__}: {path}"
        )
    for key in config:
        if not key.isidentifier():
            raise ValueError(
                f"Config key {key!r} is not a valid Python identifier: {path}"
            )
    return SimpleNamespace(**config)
