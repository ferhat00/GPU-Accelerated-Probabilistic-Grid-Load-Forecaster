"""Pytest fixtures. CI safety: force CPU paths everywhere by default."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _force_mock_gpu(monkeypatch: pytest.MonkeyPatch) -> None:
    """Default every test to MOCK_GPU=1 so CPU runners never hit GPU code paths.

    Tests that genuinely need a real GPU should be marked `@pytest.mark.gpu`
    and explicitly unset this via `monkeypatch.delenv("MOCK_GPU")`.
    """
    monkeypatch.setenv("MOCK_GPU", "1")
    # Invalidate the cached is_gpu_available result so the env change is seen.
    from gpu_grid_forecast._gpu_shim import is_gpu_available

    is_gpu_available.cache_clear()
