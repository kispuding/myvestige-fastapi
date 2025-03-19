import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "My FastAPI App")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # CORS settings (allow frontend access)
    BACKEND_CORS_ORIGINS: list = os.getenv("BACKEND_CORS_ORIGINS", "").split(",")

settings = Settings()