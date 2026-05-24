# Task runner. Run `just` with no args to see all recipes.
set windows-shell := ["bash.exe", "-c"]
set shell := ["bash", "-c"]

default:
    @just --list

# Sync the venv from pyproject + lock.
install:
    uv sync --all-extras --dev

# Quick sanity check: import + CLI help.
smoke:
    uv run python -c "import gpu_grid_forecast; print('version:', gpu_grid_forecast.__version__)"
    uv run forecast --help

# Lint (check only — does not modify files).
lint:
    uv run ruff check src tests
    uv run ruff format --check src tests

# Auto-fix lint + format.
format:
    uv run ruff format src tests
    uv run ruff check --fix src tests

# Strict type check on the package.
typecheck:
    uv run mypy src

# Full test suite with coverage.
test:
    uv run pytest tests/ -q --cov=src/gpu_grid_forecast --cov-report=term-missing

# GPU-only tests (run locally pre-push; skipped in CI).
test-gpu:
    uv run pytest tests/ -q -m gpu

# Regenerate all benchmark artifacts (phase 7).
bench:
    uv run forecast benchmark --name all

# Wipe caches and the venv.
clean:
    rm -rf .venv .ruff_cache .mypy_cache .pytest_cache build dist *.egg-info htmlcov .coverage
