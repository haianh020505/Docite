# apps/api/app/services — Business Logic Layer

The only layer that may call both repositories (for DB) and `docite_ai` (for AI).

**Belongs here:** Service classes/functions implementing domain rules (auth, document processing, chat, quota checks).
**Must NOT go here:** Direct DB queries (→ `repositories/`), HTTP primitives, or FastAPI imports.
