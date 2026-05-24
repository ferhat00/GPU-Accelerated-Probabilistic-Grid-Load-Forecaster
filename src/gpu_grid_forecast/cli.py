"""Top-level CLI. All subcommands are stubs in phase 0 and get bodies later."""

from __future__ import annotations

import typer

app = typer.Typer(
    name="forecast",
    no_args_is_help=True,
    help="GPU-accelerated probabilistic forecaster.",
    add_completion=False,
)


@app.command()
def ingest(
    source: str = typer.Option("all", help="One of: neso, era5, holidays, all."),
    year: int | None = typer.Option(None, help="Restrict to a single year."),
) -> None:
    """Download and cache raw data. (Phase 1 — stub.)"""
    typer.echo(f"[stub] ingest source={source} year={year}")


@app.command()
def features() -> None:
    """Build the modelling parquet from cached raw data. (Phase 2 — stub.)"""
    typer.echo("[stub] features")


@app.command()
def train(
    model: str = typer.Option(..., help="One of: gamlss, lgbm, nn."),
) -> None:
    """Fit a model and persist a checkpoint. (Phases 4–5 — stub.)"""
    typer.echo(f"[stub] train model={model}")


@app.command()
def evaluate(
    model: str = typer.Option(..., help="Model name matching a checkpoint."),
) -> None:
    """Compute pinball / CRPS / coverage on the test split. (Phase 3 — stub.)"""
    typer.echo(f"[stub] evaluate model={model}")


@app.command()
def benchmark(
    name: str = typer.Option("all", help="One of: kernel, training, latency, all."),
) -> None:
    """Regenerate benchmark artifacts under `artifacts/`. (Phases 6c, 7 — stub.)"""
    typer.echo(f"[stub] benchmark name={name}")
