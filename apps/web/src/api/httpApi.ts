// apps/web/src/api/httpApi.ts
// Real HTTP client that talks to apps/api over REST.
// All network calls go through this file — never fetch() directly in components.
// Base URL is read from VITE_API_BASE_URL (set in .env.local).

import type { HealthResponse } from "./types";

const BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { credentials: "include" });
  if (!res.ok) throw new Error(`HTTP ${res.status} ${path}`);
  return res.json() as Promise<T>;
}

export async function getHealth(): Promise<HealthResponse> {
  return get<HealthResponse>("/health");
}
