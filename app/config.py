from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra='allow'
    )

    DATABASE_URL: str
    PREFIX: str = '/api/v1'
    DATABASE_URI_TEST: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int


settings: Settings = Settings()
