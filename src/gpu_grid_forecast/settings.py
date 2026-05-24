"""Runtime configuration via pydantic-settings.

Reads from environment and `.env` (see `.env.example` for the full key list).
"""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Project-wide settings. Instantiate once via `get_settings()`."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    data_dir: Path = Path("data")
    artifacts_dir: Path = Path("artifacts")
    cds_api_key: str | None = None
    mock_gpu: bool = False

    @property
    def raw_dir(self) -> Path:
        return self.data_dir / "raw"

    @property
    def processed_dir(self) -> Path:
        return self.data_dir / "processed"


_cached: Settings | None = None


def get_settings() -> Settings:
    """Return the process-wide Settings singleton (lazy)."""
    global _cached
    if _cached is None:
        _cached = Settings()
    return _cached
