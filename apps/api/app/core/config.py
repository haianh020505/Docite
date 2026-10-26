"""app/core/config.py — Application configuration via pydantic-settings.

All configuration comes from environment variables (see .env.example at repo root).
Never hardcode secrets or environment-specific values here.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    secret_key: str = "CHANGE_ME"
    database_url: str = "postgresql+asyncpg://docite:docite@localhost:5432/docite"
    allowed_origins: list[str] = ["http://localhost:5173"]


settings = Settings()
