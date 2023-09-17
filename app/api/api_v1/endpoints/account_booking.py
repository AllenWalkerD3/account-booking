from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session

from app import schemas, models

router = APIRouter()


@router.get("/account-books/{book_id}", response_model=schemas.account_book.AccountBook)
async def get_account_book(book_id, db: Session = Depends(get_db)):
    account_book = models.booking.AccountBook.get_account_book(db, book_id)
    if not account_book:
        raise HTTPException(status_code=404, detail="Account Book not found")
    return account_book


@router.get("/account-books", response_model=list[schemas.account_book.AccountBook])
async def get_account_books(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return models.booking.AccountBook.get_account_books(db, skip, limit)


@router.post("/account-books", response_model=schemas.account_book.AccountBook)
def create_account_book(
    book: schemas.account_book.AccountBookCreate, db: Session = Depends(get_db)
):
    return models.booking.AccountBook.create_account_book(db=db, book=book)


@router.get(
    "/account-type/{account_type_id}", response_model=schemas.account_book.AccountType
)
async def get_account_type(account_type_id, db: Session = Depends(get_db)):
    account_type = models.booking.AccountType.get_account_type(db, account_type_id)
    if not account_type:
        raise HTTPException(status_code=404, detail="Account Type not found")
    return account_type


@router.get("/account-type", response_model=list[schemas.account_book.AccountType])
async def get_account_types(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return models.booking.AccountType.get_account_types(db, skip, limit)


@router.post("/account-type", response_model=schemas.account_book.AccountType)
def create_account_book(
    account_type: schemas.account_book.AccountTypeCreate, db: Session = Depends(get_db)
):
    return models.booking.AccountType.create_account_type(
        db=db, account_type=account_type
    )


@router.get(
    "/transactions/{transaction_id}", response_model=schemas.account_book.Transaction
)
async def get_transaction(transaction_id, db: Session = Depends(get_db)):
    transaction = models.booking.Transaction.get_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/transactions", response_model=list[schemas.account_book.Transaction])
async def get_transactions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return models.booking.Transaction.get_transactions(db, skip, limit)


@router.post("/transactions", response_model=schemas.account_book.Transaction)
def create_transaction(
    transaction: schemas.account_book.TransactionCreate, db: Session = Depends(get_db)
):
    return models.booking.Transaction.create_transaction(
        db=db,
        transaction=transaction,
        account_type_id=transaction.account_type_id,
        transaction_category_id=transaction.transaction_category_id,
        book_id=transaction.book_id,
    )



@router.get(
    "/transactions/categories/{category_id}", response_model=schemas.account_book.TransactionCategory
)
async def get_transaction_category(transaction_category_id, db: Session = Depends(get_db)):
    transaction = models.booking.TransactionCategory.get_transaction(db, transaction_category_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction Category not found")
    return transaction


@router.get("/transactions/categories", response_model=list[schemas.account_book.TransactionCategory])
async def get_transaction_categories(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return models.booking.TransactionCategory.get_transaction_categories(db, skip, limit)


@router.post("/transactions/categories", response_model=schemas.account_book.TransactionCategory)
def create_transaction_category(
    transaction_category: schemas.account_book.TransactionCategoryCreate, db: Session = Depends(get_db)
):
    return models.booking.TransactionCategory.create_transaction_category(
        db=db,
        transaction_category=transaction_category
    )