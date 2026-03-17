import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List


def load_args(config_path: str) -> List[SimpleNamespace]:
    """
    Load experiment config(s) from a JSON file and return a list of namespace objects.
    If the JSON has an ``experiments`` key, one namespace per experiment; otherwise a single namespace from the root.

    Parameters
    ----------
    config_path : str
        Path to a ``.json`` file; must have suffix ``.json``.

    Returns
    -------
    list of SimpleNamespace
        One namespace per experiment (attribute access by key); length 1 if JSON has no ``experiments`` key.

    Raises
    ------
    ValueError
        If ``config_path`` does not have suffix ``.json``.
    """
    cfg_path = Path(config_path)
    if cfg_path.suffix.lower() != ".json":
        raise ValueError(f"config_path must be a .json file, got: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # One namespace per experiment if "experiments" present; else single namespace from root
    if "experiments" in cfg:
        return [SimpleNamespace(**exp) for exp in cfg["experiments"]]
    return [SimpleNamespace(**cfg)]
