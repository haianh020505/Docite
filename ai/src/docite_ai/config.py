"""docite_ai/config.py — AI pipeline configuration constants.

These are non-secret tuning parameters. No environment variables here;
all secret/environment config lives in apps/api/app/core/config.py.
"""

from pydantic import BaseModel


class AIConfig(BaseModel):
    # Chunking
    chunk_size_tokens: int = 512
    chunk_overlap_tokens: int = 64

    # Retrieval
    top_k: int = 5
    no_source_threshold: float = 0.35  # similarity below this → "no source found"

    # Embedding model
    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536

    # Generation
    generation_model: str = "gpt-4o-mini"
    max_answer_tokens: int = 1024

    # Prompts
    prompt_language: str = "vi"  # Vietnamese


AI_CONFIG = AIConfig()
