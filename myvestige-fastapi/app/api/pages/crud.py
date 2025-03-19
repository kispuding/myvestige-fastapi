from sqlalchemy.orm import Session
from app.api.pages.models import Page
from app.api.pages.schemas import PageCreate

def create_page(db: Session, page: PageCreate):
    db_page = Page(title=page.title, content=page.content, hash=page.hash)
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page