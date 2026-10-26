"""docite_ai/types.py — Shared type definitions for the AI pipeline."""

from dataclasses import dataclass, field


@dataclass
class PageChunk:
    """A text chunk with its source metadata."""

    text: str
    document_id: str
    filename: str
    page_number: int
    chunk_index: int


@dataclass
class RetrievedChunk:
    """A chunk returned from the vector store with its similarity score."""

    chunk: PageChunk
    score: float


@dataclass
class Citation:
    """A source citation attached to an answer."""

    filename: str
    page_number: int
    excerpt: str


@dataclass
class Answer:
    """The final answer produced by the pipeline."""

    text: str
    citations: list[Citation] = field(default_factory=list)
    has_source: bool = True
