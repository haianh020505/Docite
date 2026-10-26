"""app/api/v1/chat.py — Chat router (stub).

Endpoints (to be implemented):
  GET  /v1/chat/sessions
  POST /v1/chat/sessions
  POST /v1/chat/sessions/{id}/messages

organization_id is always sourced from Depends(get_organization_id).
"""

from fastapi import APIRouter

router = APIRouter()

# TODO: implement chat endpoints
