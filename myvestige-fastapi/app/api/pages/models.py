from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    hash = Column(String, unique=True, index=True, nullable=False)