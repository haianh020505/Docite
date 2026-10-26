"""app/main.py — Application factory.

Rules:
- This file ONLY creates the FastAPI app and mounts routers.
- No business logic, no database access.
"""

from fastapi import FastAPI

from app.api.v1 import health


def create_app() -> FastAPI:
    application = FastAPI(
        title="Docite API",
        version="0.1.0",
        description="Multi-tenant Document QA SaaS API",
    )
    application.include_router(health.router, prefix="/health", tags=["health"])
    return application


app = create_app()
