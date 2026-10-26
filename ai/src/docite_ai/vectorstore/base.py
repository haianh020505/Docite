"""docite_ai/vectorstore/base.py — Abstract VectorStore interface.

CRITICAL RULE: every method that reads or writes tenant data MUST accept
`organization_id: str` as a required parameter with NO default value.
This is enforced structurally so any pgvector implementation cannot forget it.
"""

from abc import ABC, abstractmethod

from docite_ai.types import PageChunk, RetrievedChunk


class VectorStore(ABC):
    @abstractmethod
    async def upsert(
        self,
        chunks: list[PageChunk],
        embeddings: list[list[float]],
        organization_id: str,  # REQUIRED — no default
    ) -> None:
        """Store chunk embeddings tagged with organization_id."""

    @abstractmethod
    async def search(
        self,
        query_embedding: list[float],
        organization_id: str,  # REQUIRED — no default
        top_k: int,
    ) -> list[RetrievedChunk]:
        """Return top_k chunks filtered strictly to organization_id."""

    @abstractmethod
    async def delete_document(
        self,
        document_id: str,
        organization_id: str,  # REQUIRED — no default
    ) -> None:
        """Delete all chunks for a document, scoped to organization_id."""
