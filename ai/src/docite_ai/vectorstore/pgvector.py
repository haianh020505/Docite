"""docite_ai/vectorstore/pgvector.py — pgvector implementation (stub).

Uses the pgvector extension on PostgreSQL. All queries are filtered by
`organization_id` in the WHERE clause — no exceptions.
"""

from docite_ai.types import PageChunk, RetrievedChunk
from docite_ai.vectorstore.base import VectorStore


class PgVectorStore(VectorStore):
    """VectorStore backed by PostgreSQL + pgvector."""

    async def upsert(
        self,
        chunks: list[PageChunk],
        embeddings: list[list[float]],
        organization_id: str,
    ) -> None:
        # TODO: INSERT INTO embeddings (organization_id, document_id, ..., embedding)
        raise NotImplementedError

    async def search(
        self,
        query_embedding: list[float],
        organization_id: str,
        top_k: int,
    ) -> list[RetrievedChunk]:
        # TODO: SELECT ... WHERE organization_id = :org_id ORDER BY embedding <=> :vec LIMIT :k
        raise NotImplementedError

    async def delete_document(
        self,
        document_id: str,
        organization_id: str,
    ) -> None:
        # TODO: DELETE WHERE document_id = :doc_id AND organization_id = :org_id
        raise NotImplementedError
