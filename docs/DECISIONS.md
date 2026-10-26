# docs/DECISIONS.md — Architecture Decisions

One decision per line. Swap any default by updating this file and the relevant config.

| Default | Value | Reason |
|---------|-------|--------|
| Python version | 3.12 | Latest stable; `asyncio` improvements; supported by all chosen libs |
| Web framework | FastAPI | Async-first, OpenAPI auto-generation, excellent Pydantic v2 integration |
| Database | PostgreSQL 16 | Mature ACID store; pgvector extension provides native vector search |
| Vector extension | pgvector | Avoids a separate vector DB service; simplifies the deployment stack |
| Database migrations | Alembic | Standard SQLAlchemy migration tool; supports async engines |
| ORM | SQLAlchemy 2 (async) | Type-safe mapped columns; async-native; pairs cleanly with Alembic |
| Config management | pydantic-settings | Type-safe env var parsing; auto `.env` loading; consistent with Pydantic v2 |
| Linter/formatter | ruff | Replaces flake8+isort+pyupgrade in one fast binary |
| Test runner | pytest | Industry standard; rich ecosystem (pytest-asyncio, httpx TestClient) |
| Embedding model | text-embedding-3-small | Cost-effective; swappable via `AI_CONFIG.embedding_model` |
| LLM | gpt-4o-mini | Low latency, low cost for Q&A; swappable via `AI_CONFIG.generation_model` |
| Prompt language | Vietnamese | Target user base; prompts versioned as `.md` files in `ai/src/docite_ai/prompts/` |
| No-source threshold | 0.35 cosine similarity | Conservative default; tune via evaluation in `evals/` |
| Container runtime | Docker Compose | Simple local dev; db-first compose order; API/web services commented for later |
