from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session

from app import schemas, models

router = APIRouter()


@router.get("/{user_id}", response_model=schemas.users.User)
async def get_users(user_id, db: Session = Depends(get_db)):
    user = models.auth.User.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[schemas.users.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return models.auth.User.get_users(db, skip, limit)


@router.post("/", response_model=schemas.users.User)
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = models.auth.User.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return models.auth.User.create_user(db=db, user=user)
