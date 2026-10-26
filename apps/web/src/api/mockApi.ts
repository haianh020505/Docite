// apps/web/src/api/mockApi.ts
// In-memory mock of the HTTP API for local development without a running backend.
// Import and use the same function signatures as httpApi.ts.
// Must NOT be imported in production builds.

import type { HealthResponse } from "./types";

export async function getHealth(): Promise<HealthResponse> {
  return { status: "ok", version: "mock" };
}
