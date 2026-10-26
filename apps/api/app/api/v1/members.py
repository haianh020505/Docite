"""app/api/v1/members.py — Members/org management router (stub).

Endpoints (to be implemented):
  GET    /v1/members
  POST   /v1/members/invite
  DELETE /v1/members/{id}
  PATCH  /v1/members/{id}/role

organization_id is always sourced from Depends(get_organization_id).
"""

from fastapi import APIRouter

router = APIRouter()

# TODO: implement member endpoints
