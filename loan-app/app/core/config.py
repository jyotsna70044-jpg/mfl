from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/loan_db"
    DATABASE_URL: str = "postgresql + asyncpg://postgres:postgres123@db:5432/loan_db"
    SECRET_KEY: str = "change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
