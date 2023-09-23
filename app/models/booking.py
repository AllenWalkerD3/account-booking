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
    def create_account_book(
        cls, db: Session, book: schemas.account_book.AccountBookCreate
    ):
        db_book = cls(book_name=book.book_name, user_id=book.user_id)
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
    def create_account_type(
        cls, db: Session, account_type: schemas.account_book.AccountTypeCreate
    ):
        db_accout_type = cls(name=account_type.name)
        db.add(db_accout_type)
        db.commit()
        db.refresh(db_accout_type)
        return db_accout_type


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float)
    transaction_type = Column(String, nullable=False, default="debit")
    datetime = Column(DateTime, default=datetime.datetime.utcnow)

    account_type_id = Column(Integer, ForeignKey("account_types.id"))
    account_type = relationship("AccountType", back_populates="transactions")

    transaction_category_id = Column(Integer, ForeignKey("account_categories.id"))
    transaction_category = relationship(
        "TransactionCategory", back_populates="transactions"
    )

    book_id = Column(Integer, ForeignKey("account_books.id"))
    book = relationship("AccountBook", back_populates="transactions")

    @classmethod
    def get_transaction(cls, db: Session, transaction_id: int):
        return db.query(cls).filter(cls.id == transaction_id).first()

    @classmethod
    def get_transactions(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(cls).offset(skip).limit(limit).all()

    @classmethod
    def create_transaction(
        cls, db: Session, transaction: schemas.account_book.TransactionCreate
    ):
        db_transaction = cls(**transaction.__dict__)
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction


class TransactionCategory(Base):
    __tablename__ = "account_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="transaction_category")

    @classmethod
    def get_transaction_category(cls, db: Session, transaction_category_id: int):
        return db.query(cls).filter(cls.id == transaction_category_id).first()

    @classmethod
    def get_transaction_categories(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(cls).offset(skip).limit(limit).all()

    @classmethod
    def create_transaction_category(
        cls,
        db: Session,
        transaction_category: schemas.account_book.TransactionCategoryCreate,
    ):
        db_transaction_category = cls(
            name=transaction_category.name, color=transaction_category.color
        )
        db.add(db_transaction_category)
        db.commit()
        db.refresh(db_transaction_category)
        return db_transaction_category
