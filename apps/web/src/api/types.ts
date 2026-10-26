// apps/web/src/api/types.ts
// Shared TypeScript types that mirror Pydantic schemas in apps/api/app/schemas/.
// Keep in sync with the Python side manually (or via generated openapi-ts later).
// No implementation — types only.

export type OrganizationId = string; // UUID

export interface HealthResponse {
  status: "ok";
  version: string;
}
