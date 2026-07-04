from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "RISE API"
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://rise:rise_dev_password@postgres:5432/rise"
    redis_url: str = "redis://redis:6379/0"
    secret_key: str = Field(
        default="development-secret-key-change-before-production", min_length=32
    )
    access_token_expire_minutes: int = 30
    seed_admin_email: str = "admin@rise.local"
    seed_admin_password: str = "ChangeMe123!"
    cors_origins: list[str] = ["http://localhost:3000"]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
