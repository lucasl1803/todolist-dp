from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import CRUD.category_crud as category_crud
import schemas


router = APIRouter(prefix="/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Category])
def list_categories(db: Session = Depends(get_db)):
    return category_crud.get_categories(db)


@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return category_crud.create_category(db, category)

