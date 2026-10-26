# docs/api-contract.md — Docite API Contract

> **Status:** Headings-only scaffold. Paste the full contract here.

All communication between `apps/web` and `apps/api` follows this contract.
TypeScript types in `apps/web/src/api/types.ts` must mirror the Pydantic schemas defined here.

---

## Authentication

### POST /v1/auth/register
### POST /v1/auth/login
### POST /v1/auth/logout
### POST /v1/auth/refresh

---

## Health

### GET /health

---

## Documents

### GET /v1/documents
### POST /v1/documents
### GET /v1/documents/{document_id}
### DELETE /v1/documents/{document_id}

---

## Chat

### GET /v1/chat/sessions
### POST /v1/chat/sessions
### POST /v1/chat/sessions/{session_id}/messages

---

## Members

### GET /v1/members
### POST /v1/members/invite
### DELETE /v1/members/{member_id}
### PATCH /v1/members/{member_id}/role

---

## Common Conventions

- All timestamps: ISO 8601 UTC (`2024-01-01T00:00:00Z`)
- All IDs: UUID v4 strings
- Errors: `{"detail": "message"}` (FastAPI default)
- Auth: Bearer token in `Authorization` header
- Pagination: `?page=1&page_size=20` where applicable
