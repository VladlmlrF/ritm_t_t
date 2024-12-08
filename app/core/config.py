from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


settings = Settings()
