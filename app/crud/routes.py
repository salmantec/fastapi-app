from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from . import repo
from ..db_connection import get_db

router = APIRouter(prefix="/api/v1")


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = repo.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repo.create_user(db=db, user=user)
