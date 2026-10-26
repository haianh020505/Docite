# apps/api — Docite FastAPI Backend

HTTP API server for the Docite SaaS platform.

**Belongs here:** FastAPI routers, dependency injection, Pydantic schemas, SQLAlchemy models, Alembic migrations, services, repositories, background workers, and file-storage abstraction.
**Must NOT go here:** UI code, business logic in routers (put it in `services/`), direct DB access in services (put it in `repositories/`), or anything that imports `ai/` beyond the public `docite_ai` package API.

## Layers (enforced by convention)
```
api/ (HTTP)  →  services/ (business logic)  →  repositories/ (DB)
                                             ↘  docite_ai (RAG)
```

## Dev
```powershell
cd apps/api
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e . -e ../../ai
uvicorn app.main:app --reload   # http://localhost:8000
pytest                          # run all tests
ruff check .                    # lint
```
