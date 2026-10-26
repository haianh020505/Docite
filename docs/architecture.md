# docs/architecture.md — Docite System Architecture

## Overview

Docite is a multi-tenant Document QA SaaS.  
Each organization uploads PDFs; users ask questions; the AI answers **only** from that organization's documents, citing file name and page number.  
One organization must never see another's data.

## Boundary Rules

| Rule | Description |
|------|-------------|
| **HTTP only** | `web` ↔ `api` communicate exclusively over HTTP following `docs/api-contract.md` |
| **Layer discipline** | `api/` routers → `services/` → `repositories/` (DB). No skipping layers. |
| **AI isolation** | `ai/` never imports FastAPI, SQLAlchemy, or anything from `apps/api`. |
| **Org scoping** | Every tenant-data function in `repositories/` and `ai/vectorstore/` takes `organization_id` as a **required** parameter with **no default**. |
| **Prompt versioning** | All prompts are files in `ai/src/docite_ai/prompts/`; never inline strings. |
| **No secrets in repo** | `.env.example` only; all config via pydantic-settings. |
| **Synthetic data only** | No real tenant documents or org names in git. |

---

## Diagram A — Document Ingestion Pipeline

```mermaid
flowchart TD
    Upload["📤 User uploads PDF\n(POST /v1/documents)"]
    Store["💾 Store file\n(storage/)"]
    Worker["⚙️ Background worker\n(workers/ingest_document)"]
    Extract["📄 Extract pages\n(docite_ai/ingestion)"]
    Chunk["✂️ Chunk text\nwith page numbers\n(docite_ai/chunking)"]
    Embed["🔢 Generate embeddings\n(docite_ai/embeddings)"]
    VectorStore["🗄️ Store in vectorstore\ntagged with organization_id\n(docite_ai/vectorstore/pgvector)"]
    StatusReady["✅ Status → Ready"]
    StatusFailed["❌ Status → Failed"]

    Upload --> Store
    Store --> Worker
    Worker --> Extract
    Extract --> Chunk
    Chunk --> Embed
    Embed --> VectorStore
    VectorStore --> StatusReady
    Extract -. "error" .-> StatusFailed
    Chunk -. "error" .-> StatusFailed
    Embed -. "error" .-> StatusFailed
    VectorStore -. "error" .-> StatusFailed
```

---

## Diagram B — Question Answering Pipeline

```mermaid
flowchart TD
    Question["❓ User asks question\n(POST /v1/chat/sessions/{id}/messages)"]
    Retrieve["🔍 Retrieve chunks\nfiltered by organization_id\n(docite_ai/retrieval)"]
    Threshold{"Similarity ≥ threshold?"}
    NoSource["🚫 No source found\n(docite_ai/guardrails)\nReturn: 'Không tìm thấy...'"]
    Generate["🤖 Generate answer\n(docite_ai/generation)\nUsing versioned Vietnamese prompt"]
    Citations["📎 Build citations\nfile name + page number\n(docite_ai/generation)"]
    Response["📨 Answer with citations\nreturned to user"]

    Question --> Retrieve
    Retrieve --> Threshold
    Threshold -- "below threshold" --> NoSource
    Threshold -- "above threshold" --> Generate
    Generate --> Citations
    Citations --> Response
    NoSource --> Response
```
