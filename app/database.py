from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


POSTGRESSQL_URL = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="account_booking",
    port=5433,
)
engine = create_engine(POSTGRESSQL_URL)


# SQLALCHEMY_DATABASE_URL = "s3://account-booking-v1-stagi-serverlessdeploymentbuck-6os1hrq3fy1b/sql_account_booking.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_account_booking.db"


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db(request: Request):
    return request.state.db
