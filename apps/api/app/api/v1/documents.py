"""app/api/v1/documents.py — Documents router (stub).

Endpoints (to be implemented):
  GET    /v1/documents
  POST   /v1/documents          (upload PDF)
  GET    /v1/documents/{id}
  DELETE /v1/documents/{id}

organization_id is always sourced from Depends(get_organization_id).
"""

from fastapi import APIRouter

router = APIRouter()

# TODO: implement document endpoints
