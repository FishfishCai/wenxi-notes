import random

import numpy as np
import torch


def set_seed(
    seed: int,
) -> None:
    """
    Set random seeds for Python, NumPy, and PyTorch (CPU + CUDA) to ensure reproducibility.

    Parameters
    ----------
    seed : int
        Global random seed applied to all backends.

    Returns
    -------
    None
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
