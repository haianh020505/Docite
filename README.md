# Docite

**Multi-tenant Document QA SaaS** — Organizations upload PDFs; users ask questions; the AI answers only from that organization's documents and cites file name + page. One organization never sees another's data.

---

## Repository Structure

| Folder | Purpose |
|--------|---------|
| `apps/web/` | Vite + React + TS + Tailwind v4 SPA |
| `apps/api/` | FastAPI backend (HTTP, business logic, DB) |
| `ai/` | Pure Python RAG core (`docite_ai` package) |
| `evals/` | Offline quality evaluation (golden datasets, metrics) |
| `notebooks/` | Experiments — strip outputs before commit |
| `data/samples/` | Synthetic PDFs for dev/testing only |
| `scripts/` | Dev helpers (seeding, etc.) |
| `infra/` | docker-compose.yml (pgvector db) |
| `docs/` | Architecture, decisions, API contract, runbook |

---

## Quick Start (PowerShell)

### 1 — Database
```powershell
cd infra
docker compose up db -d
```

### 2 — API backend
```powershell
cd apps/api
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e . -e ../../ai
Copy-Item .env.example .env   # then edit SECRET_KEY etc.
uvicorn app.main:app --reload
# Open http://localhost:8000/docs
```

### 3 — Frontend
```powershell
cd apps/web
npm install
npm run dev
# Open http://localhost:5173
```

### 4 — Tests
```powershell
# API tests (from apps/api with venv active)
pytest -v

# AI tests (from ai with venv active)
cd ai; pytest -v

# Frontend
cd apps/web; npm run lint; npx tsc --noEmit; npm run build

# Evaluations
cd evals; python run_eval.py
```

### 5 — Lint
```powershell
# Python (run from apps/api or ai)
ruff check .
ruff check --fix .   # auto-fix

# TypeScript
cd apps/web; npm run lint
```

---

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for Mermaid diagrams of the ingestion and query pipelines.

## Decisions

See [`docs/DECISIONS.md`](docs/DECISIONS.md) for all architectural defaults and their rationale.

## Tenancy & Privacy

See [`docs/tenancy-and-privacy.md`](docs/tenancy-and-privacy.md) for the data isolation rules and required security tests.
