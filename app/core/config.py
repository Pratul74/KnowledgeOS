from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    app_name: str
    app_env: str
    app_debug: bool = False
    app_version: str

    host: str
    port: int

    api_prefix: str

    secret_key: str
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int
    refresh_token_expire_days: int

    encryption_key: str

    database_url: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()