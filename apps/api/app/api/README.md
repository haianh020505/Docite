# apps/api/app/api — HTTP Layer

FastAPI routers only. Business logic goes in `services/`.

**Belongs here:** Router files (`v1/*.py`), shared dependencies (`deps.py`).
**Must NOT go here:** Business logic, DB queries, or AI calls. Routers call services only.
