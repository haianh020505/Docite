# ai — Docite AI / RAG Core

Pure Python package (`docite_ai`) containing the entire AI pipeline.

**Belongs here:** PDF ingestion, chunking, embedding, vector search, retrieval, LLM generation, citation building, prompts, guardrails.
**Must NOT go here:** FastAPI, SQLAlchemy, HTTP handlers, secrets, or anything from `apps/`.
`apps/api` installs this package with `pip install -e ../../ai`.

## Boundary rule
Every function in `vectorstore/` and `retrieval/` that touches tenant data MUST accept
`organization_id: str` as a **required** parameter with **no default value**.

## Dev
```powershell
cd ai
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
ruff check src/
```
