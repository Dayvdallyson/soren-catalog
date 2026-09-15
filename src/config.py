from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_URL: str = "postgresql+psycopg2://soren:soren@localhost:5432/catalog"
  REDIS_URL: str = "redis://localhost:6379/0"
  MEILI_URL: str = "http://localhost:7700"
  MEILI_KEY: str = "dev_master_key"
  SMTP_HOST: str = "localhost"
  SMTP_PORT: int = 1025

settings = Settings()
