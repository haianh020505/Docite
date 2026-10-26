"""app/api/deps.py — Shared FastAPI dependencies.

Use these via Depends() in routers.
- get_db: async database session
- get_current_user: authenticated user (raises 401 if not)
- get_organization_id: validated org UUID from the authenticated session
  NOTE: organization_id MUST come only from this dependency, never from
  request bodies, query strings, or URL path parameters.
"""

from fastapi import Depends  # noqa: F401 — re-exported for routers


# TODO: implement after DB layer is wired
async def get_db():  # type: ignore[empty-body]
    """Yield an async SQLAlchemy session."""
    raise NotImplementedError


async def get_current_user(db=Depends(get_db)):  # type: ignore[empty-body]  # noqa: B008
    """Return the authenticated user or raise HTTP 401."""
    raise NotImplementedError


async def get_organization_id(current_user=Depends(get_current_user)) -> str:  # noqa: B008
    """Extract organization_id from the authenticated session.

    This is the ONLY legitimate source of organization_id in route handlers.
    """
    raise NotImplementedError

