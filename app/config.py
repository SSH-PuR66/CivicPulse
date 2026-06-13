from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    census_api_key: str = ""
    cache_ttl_seconds: int = 3600
    census_base_url: str = "https://api.census.gov/data/2022/acs/acs5"

    class Config:
        env_file = ".env"


settings = Settings()
