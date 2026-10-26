# docs/tenancy-and-privacy.md — Multi-Tenancy & Privacy Rules

## Core Rules

### Rule 4 — organization_id Scoping

Every function in `repositories/` and `ai/vectorstore/` that reads or writes tenant data
MUST take `organization_id` as a **required** parameter with **no default value**.

The `organization_id` MUST originate exclusively from the authenticated session dependency
(`apps/api/app/api/deps.py::get_organization_id`).

It MUST NOT come from:
- Request bodies
- Query string parameters
- URL path parameters
- Any client-supplied value

**Rationale:** Prevents a confused-deputy attack where a client tricks the server into
accessing another tenant's data by supplying a different org ID.

### Rule 7 — Data in Git

Only synthetic, anonymous sample data may be committed to the repository:
- `data/samples/` — small synthetic PDFs, no real org names, no PII
- `evals/datasets/` — synthetic golden Q&A pairs only

Real tenant documents, real organization names, and any PII are **permanently prohibited**
from the repository.

---

## Required Security Tests

The following tests MUST exist in `apps/api/tests/security/` before any release:

| Test | Description |
|------|-------------|
| `test_cross_tenant_retrieval` | Query from Org A never returns chunks belonging to Org B |
| `test_cross_tenant_documents` | `GET /v1/documents` for Org A never lists Org B's documents |
| `test_forbidden_role_invite` | A user with role `member` cannot call `POST /v1/members/invite` (expects 403) |
| `test_forbidden_role_remove` | A user with role `member` cannot call `DELETE /v1/members/{id}` (expects 403) |
| `test_no_auth_rejected` | All protected endpoints return 401 without a valid token |

---

## Enforcement Checklist

- [ ] `organization_id` parameter type is `uuid.UUID` (not `str`) in all repository functions
- [ ] CI `security/` tests run in the `api` job
- [ ] ruff is configured to reject wildcard imports (`*`) in repositories
- [ ] Alembic migrations always add `organization_id` FK to tenant tables
