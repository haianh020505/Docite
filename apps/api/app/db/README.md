# apps/api/app/db — Database Infrastructure

SQLAlchemy engine, session factory, declarative base, and Alembic migrations.

**Belongs here:** `session.py`, `base.py`, `migrations/` (Alembic).
**Must NOT go here:** ORM model definitions (those live in `models/`), business logic, or queries (those live in `repositories/`).
