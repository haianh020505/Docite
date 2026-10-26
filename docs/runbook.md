# docs/runbook.md — Operational Runbook

## Starting Services (Local Dev)

### 1. Database
```powershell
cd infra
docker compose up db -d
docker compose ps   # wait for db to be healthy
```

### 2. API Backend
```powershell
cd apps/api
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e . -e ../../ai
# Copy and edit env:
Copy-Item .env.example .env
uvicorn app.main:app --reload
# → http://localhost:8000/docs
```

### 3. Frontend
```powershell
cd apps/web
npm install
npm run dev
# → http://localhost:5173
```

## Running Tests

```powershell
# API tests
cd apps/api; pytest -v

# AI tests
cd ai; pytest -v

# Frontend lint + typecheck
cd apps/web; npm run lint; npx tsc --noEmit

# Evaluations
cd evals; python run_eval.py
```

## Database Migrations

```powershell
cd apps/api
# Generate new migration:
alembic revision --autogenerate -m "describe change"
# Apply:
alembic upgrade head
# Rollback one step:
alembic downgrade -1
```

## Common Issues

| Issue | Fix |
|-------|-----|
| `asyncpg` can't connect | Ensure `docker compose up db -d` is running |
| `ruff` errors in CI | Run `ruff check --fix .` locally first |
| Build warning about `__dirname` | Use `import.meta.dirname` (already fixed in `vite.config.ts`) |
