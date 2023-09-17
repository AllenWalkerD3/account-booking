from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship, Session
import datetime


from app import schemas

from ..database import Base

class AccountBook(Base):

    __tablename__ = "account_books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="account_books")

    transactions = relationship("Transaction", back_populates="book")

    @classmethod
    def get_account_book(cls, db: Session, book_id: int):
        return db.query(cls).filter(cls.id == book_id).first()
    
    @classmethod
    def get_account_books(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(cls).offset(skip).limit(limit).all()
    
    @classmethod
    def create_account_book(cls, db: Session, book: schemas.account_book.AccountBookCreate):
        db_book = cls(book_name = book.book_name, user_id = book.user_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

class AccountType(Base):
    __tablename__ = "account_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    transactions = relationship("Transaction", back_populates="account_type")

    @classmethod
    def get_account_type(cls, db: Session, account_type_id: int):
        return db.query(cls).filter(cls.id == account_type_id).first()
    
    @classmethod
    def get_account_types(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(cls).offset(skip).limit(limit).all()
    
    @classmethod
    def create_account_type(cls, db: Session, account_type: schemas.account_book.AccountTypeCreate):
        db_book = cls(name = account_type.name)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    decription = Column(String, nullable=False)
    amount = Column(Float)
    transaction_type = Column(String, nullable=False, default="debit")
    datetime = Column(DateTime, default=datetime.datetime.utcnow)

    account_type_id = Column(Integer, ForeignKey("account_types.id"))
    account_type = relationship("AccountType", back_populates="transactions")

    transaction_category_id = Column(Integer, ForeignKey("account_categories.id"))
    transaction_category = relationship("TransactionCategory", back_populates="transactions")

    book_id = Column(Integer, ForeignKey("account_books.id"))
    book = relationship("AccountBook", back_populates="transactions")

class TransactionCategory(Base):
    __tablename__ = "account_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="transaction_category")