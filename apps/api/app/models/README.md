# apps/api/app/models — SQLAlchemy ORM Models

One file per domain entity. All tenant-scoped tables include a non-nullable `organization_id` FK.

**Belongs here:** SQLAlchemy `Mapped` model classes.
**Must NOT go here:** Pydantic schemas (→ `schemas/`), queries (→ `repositories/`), business logic (→ `services/`).
