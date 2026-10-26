"""app/core/logging.py — Structured logging setup (stub).

Will configure structlog or the standard library logging for JSON output.
Import `logger` from here; do not configure logging elsewhere.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("docite")
