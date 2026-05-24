"""Smoke test: package imports + CLI shows all subcommands."""

from __future__ import annotations

from typer.testing import CliRunner

import gpu_grid_forecast
from gpu_grid_forecast._gpu_shim import is_gpu_available
from gpu_grid_forecast.cli import app
from gpu_grid_forecast.settings import get_settings


def test_package_has_version() -> None:
    assert gpu_grid_forecast.__version__
    assert gpu_grid_forecast.__version__.count(".") == 2


def test_cli_help_lists_all_subcommands() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for cmd in ("ingest", "features", "train", "evaluate", "benchmark"):
        assert cmd in result.stdout, f"`{cmd}` missing from `forecast --help`"


def test_cli_stubs_invoke_without_error() -> None:
    runner = CliRunner()
    for argv in (
        ["ingest", "--source", "holidays"],
        ["features"],
        ["train", "--model", "gamlss"],
        ["evaluate", "--model", "gamlss"],
        ["benchmark", "--name", "all"],
    ):
        result = runner.invoke(app, argv)
        assert result.exit_code == 0, f"{argv} failed: {result.stdout}"


def test_mock_gpu_fixture_is_respected() -> None:
    # conftest sets MOCK_GPU=1 by default; the shim must agree.
    assert is_gpu_available() is False


def test_settings_load_with_defaults() -> None:
    s = get_settings()
    assert s.data_dir.name == "data"
    assert s.raw_dir.parts[-2:] == ("data", "raw")
    assert s.processed_dir.parts[-2:] == ("data", "processed")
