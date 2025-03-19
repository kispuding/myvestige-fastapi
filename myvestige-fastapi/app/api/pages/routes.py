from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.pages import crud, schemas

router = APIRouter()

@router.post("/pages/")
def create_page(page: schemas.PageCreate, db: Session = Depends(get_db)):
    return crud.create_page(db=db, page=page)