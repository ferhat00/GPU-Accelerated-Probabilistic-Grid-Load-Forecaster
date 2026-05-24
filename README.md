# GPU-Accelerated Probabilistic Grid Load Forecaster

> Status: **early scaffolding** — phase 0 complete. Headline chart + numbers land in phase 7.

<!-- HEADLINE_CHART -->

Probabilistic short-term forecasts of UK national electricity demand at 30 min / 1 h / 6 h / 24 h horizons. Outputs **full predictive distributions** (sinh-arcsinh family), not point predictions, evaluated by pinball loss, CRPS, and 80% / 95% PI coverage.

The point of the repo is to show three things together in one place: probabilistic-forecasting depth carried over from GAMLSS-on-crude work at Argus Media; real NVIDIA stack proficiency (RAPIDS, LightGBM-GPU, PyTorch, custom CUDA); and engineering rigour (typed Python, tests, CI, reproducible benchmarks).

## Build phases

- [x] **Phase 0** — Toolchain & project skeleton
- [ ] Phase 1 — Data ingestion (NESO, ERA5, bank holidays)
- [ ] Phase 2 — Feature builder + splits
- [ ] Phase 3 — Evaluation harness (pinball, CRPS, reliability)
- [ ] Phase 4a — GAMLSS CPU baseline (rpy2)
- [ ] Phase 4b — LightGBM-GPU multi-quantile
- [ ] Phase 5 — PyTorch sinh-arcsinh MLP (naive NLL — CUDA kernel reference)
- [ ] Phase 6a — Custom CUDA kernel (naive) + validation harness
- [ ] Phase 6b — Optimised CUDA kernel
- [ ] Phase 6c — Headline kernel benchmark
- [ ] Phase 7 — Cross-model benchmark suite + README polish

Full plan: see `docs/PLAN.md` (to be copied in from the planning artifact in phase 1).

## Development

Requires **Python 3.11**, [`uv`](https://docs.astral.sh/uv/), and [`just`](https://github.com/casey/just). CUDA 12.x toolkit needed for phases 4b–6c (recommended via WSL2 on Windows).

```bash
just install     # uv sync the env from pyproject + lock
just smoke       # quick import + CLI sanity check
just test        # pytest with coverage
just lint        # ruff check + format check
just typecheck   # strict mypy on src/
```

Pre-work for phase 1: register for a [Copernicus CDS API key](https://cds.climate.copernicus.eu/api-how-to) — approval typically takes ~24 h. Add the key to a local `.env` (see `.env.example`).

### Environment

| Layer        | Local dev (WSL2 / Linux)         | CI (GitHub Actions)        |
|--------------|----------------------------------|----------------------------|
| Python       | 3.11 (via `uv python install`)   | 3.11                       |
| GPU          | local consumer card + rented A100/H100 for phase 6c headline | none (`MOCK_GPU=1`) |
| CUDA toolkit | 12.x (`nvcc` required for phase 6) | n/a                      |
| R            | `r-base` + `gamlss` (phase 4a)   | not installed              |

## Methods, results, references

To be written in phase 7. Math anchor for the sinh-arcsinh distribution: Jones & Pewsey (2009), *Sinh-arcsinh distributions*, **Biometrika** 96(4): 761–780.
