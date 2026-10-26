# apps/api/app/repositories — Database Access Layer

All SQL queries live here. Every public function that touches tenant data takes `organization_id: uuid.UUID` as a **required** parameter with **no default**.

**Belongs here:** SQLAlchemy async query functions, one file per domain entity.
**Must NOT go here:** Business logic, FastAPI imports, AI calls, or functions without an `organization_id` parameter on tenant data.
