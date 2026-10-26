"""app/api/v1/health.py — Health check endpoint.

GET /health  →  {"status": "ok", "version": "0.1.0"}

This is the only implemented endpoint in the scaffold.
No auth required; used by load-balancers and CI smoke tests.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    version: str


@router.get("", response_model=HealthResponse, summary="Health check")
async def get_health() -> HealthResponse:
    return HealthResponse(status="ok", version="0.1.0")
