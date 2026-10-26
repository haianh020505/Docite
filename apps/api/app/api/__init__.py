"""app/api — HTTP layer.

Routers live in v1/.  Shared FastAPI dependencies live in deps.py.
Rules:
- Routers call services, never repositories directly.
- No business logic in this layer.
"""
