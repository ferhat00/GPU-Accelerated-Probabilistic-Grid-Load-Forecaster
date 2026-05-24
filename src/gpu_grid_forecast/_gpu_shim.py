"""Single import surface for GPU-conditional code.

When `MOCK_GPU=1` or no CUDA device is present, GPU paths must fall back to
CPU equivalents. Modules that touch the GPU import from here rather than from
`torch.cuda` / `cudf` directly, so the fallback is centralised and testable.
"""

from __future__ import annotations

import os
from functools import lru_cache


def _mock_gpu_env() -> bool:
    return os.environ.get("MOCK_GPU", "0").lower() in {"1", "true", "yes"}


@lru_cache(maxsize=1)
def is_gpu_available() -> bool:
    """Return True iff a real CUDA device is usable AND MOCK_GPU is not set.

    Result is cached for the life of the process; tests that flip `MOCK_GPU`
    via `monkeypatch.setenv` must also call `is_gpu_available.cache_clear()`.
    """
    if _mock_gpu_env():
        return False
    try:
        import torch
    except ImportError:
        return False
    return bool(torch.cuda.is_available())


def require_gpu() -> None:
    """Raise if no GPU is available. Use at the entry of GPU-only code paths."""
    if not is_gpu_available():
        raise RuntimeError(
            "CUDA GPU required but unavailable "
            "(MOCK_GPU env var or no CUDA device). "
            "Either run on a CUDA machine or use the CPU fallback explicitly."
        )
