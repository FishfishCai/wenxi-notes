import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List


def load_args(
    config_path: str,
) -> List[SimpleNamespace]:
    """
    Load experiment configuration from a JSON file and return one ``SimpleNamespace`` per experiment entry.

    Parameters
    ----------
    config_path : str
        Path to a ``.json`` file; must use the ``.json`` suffix.

    Returns
    -------
    experiment_configs : list of SimpleNamespace
        One namespace per experiment when the root object has an ``"experiments"`` list; otherwise a
        single-element list built from the root object.

    Raises
    ------
    ValueError
        If ``config_path`` does not end with ``.json``.
    """
    cfg_path = Path(config_path)
    if cfg_path.suffix.lower() != ".json":
        raise ValueError(f"config_path must be a .json file, got: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # Root ``experiments`` list vs single root dict
    if "experiments" in cfg:
        return [SimpleNamespace(**exp) for exp in cfg["experiments"]]
    return [SimpleNamespace(**cfg)]
