"""docite_ai/pipeline.py — Public API of the docite_ai package.

Two functions form the public contract:
  ingest_document(document_id, organization_id, filename, file_bytes) -> None
  answer_question(question, organization_id) -> Answer

All AI pipeline steps are orchestrated here. This module is the only place
apps/api needs to import from; internal sub-modules are implementation details.
"""

from docite_ai.types import Answer


async def ingest_document(
    document_id: str,
    organization_id: str,  # REQUIRED — no default
    filename: str,
    file_bytes: bytes,
) -> None:
    """Extract pages → chunk → embed → store in vectorstore tagged with organization_id."""
    # TODO: wire ingestion → chunking → embeddings → vectorstore
    raise NotImplementedError


async def answer_question(
    question: str,
    organization_id: str,  # REQUIRED — no default
) -> Answer:
    """Retrieve context filtered by organization_id → generate answer with citations."""
    # TODO: wire retrieval → guardrails → generation → citation builder
    raise NotImplementedError
