from pydantic import BaseModel
import datetime


# region Account Type
class AccountTypeBase(BaseModel):
    name: str


class AccountTypeCreate(AccountTypeBase):
    pass


class AccountType(AccountTypeBase):
    id: int

    class Config:
        from_attributes = True


# endregion


# region Account Category
class TransactionCategoryBase(BaseModel):
    name: str
    color: str


class TransactionCategoryCreate(TransactionCategoryBase):
    pass


class TransactionCategory(TransactionCategoryBase):
    id: int

    class Config:
        from_attributes = True


# endregion


# region Transaction
class TransactionBase(BaseModel):
    description: str
    amount: float
    transaction_type: str
    account_type_id: int
    transaction_category_id: int
    book_id: int


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    datetime: datetime.datetime
    account_type: AccountType
    transaction_category: TransactionCategory

    class Config:
        from_attributes = True


# endregion


# region Account Book
class AccountBookBase(BaseModel):
    book_name: str
    user_id: int


class AccountBookCreate(AccountBookBase):
    pass


class AccountBook(AccountBookBase):
    id: int
    transactions: list[Transaction] = []

    class Config:
        from_attributes = True


# endregion