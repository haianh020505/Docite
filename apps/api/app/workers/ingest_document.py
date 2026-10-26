"""app/workers/ingest_document.py — Document ingestion background job (stub).

Triggered after a file is uploaded. Workflow:
  1. Download raw file from storage
  2. Call docite_ai.pipeline.ingest_document()
  3. Update document status to "ready" or "failed"
"""

import uuid

# TODO: implement after docite_ai pipeline is ready


async def ingest_document(document_id: uuid.UUID, organization_id: uuid.UUID) -> None:
    """Process a newly uploaded document through the AI ingestion pipeline."""
    raise NotImplementedError
