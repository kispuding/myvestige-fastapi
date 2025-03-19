from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Database connection URL (reads from environment variables)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://debug:debug@localhost:5432/myvestige")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries (useful for debugging)

# SQLAlchemy Base Model
Base = declarative_base()