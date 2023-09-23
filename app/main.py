import os
from typing import Union

from fastapi import FastAPI, Request, Response
from mangum import Mangum

from .api.api_v1.api import router as api_router
from .database import SessionLocal, engine
from .models import Base

Base.metadata.create_all(bind=engine)
stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="AccountBooking", openapi_prefix=openapi_prefix)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(api_router, prefix="/api/v1")
app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app)
