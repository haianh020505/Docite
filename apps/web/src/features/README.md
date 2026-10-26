# apps/web/src/features — Feature Modules

One folder per product feature. Each feature is self-contained: its own components, hooks, and local state.

**Belongs here:** `auth/`, `chat/`, `documents/`, `members/`, `landing/` feature folders.
**Must NOT go here:** Shared utilities (→ `lib/`), shared hooks (→ `hooks/`), or UI primitives (→ `components/ui/`).

Each sub-folder may contain: `components/`, `hooks/`, `stores/`, `index.ts`.
