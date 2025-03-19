from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.db.database import DATABASE_URL

# Create an async engine (for asynchronous DB operations)
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory
async_session_maker = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get DB session in FastAPI routes
async def get_db():
    async with async_session_maker() as session:
        yield session