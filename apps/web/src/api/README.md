# apps/web/src/api — Network Layer

The **only** place that makes HTTP calls. All components use this layer.

**Belongs here:** `types.ts` (TypeScript types mirroring backend schemas), `httpApi.ts` (real fetch calls), `mockApi.ts` (in-memory mock for development).
**Must NOT go here:** React components, business logic, or direct `fetch()` calls outside this folder.
