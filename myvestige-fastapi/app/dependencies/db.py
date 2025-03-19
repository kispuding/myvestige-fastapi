from app.db.session import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

def get_db_dependency() -> AsyncSession:
    """Dependency to get a database session."""
    return Depends(get_db)