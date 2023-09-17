from pydantic import BaseModel

from app.schemas.account_book import AccountBook

class UserBase(BaseModel):
    username: str
    email: str
    sub: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    account_books: list[AccountBook] = []

    class Config:
        from_attributes = True