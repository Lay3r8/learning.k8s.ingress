
"""
Holds all backend settings
"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Base settings for the application"""
    API_PREFIX: str = "/api"
    VERSION: str = "0.1.0"
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    """Returns app settings"""
    return Settings()
