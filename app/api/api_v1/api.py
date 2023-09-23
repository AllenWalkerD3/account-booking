from fastapi import APIRouter

from .endpoints import users, account_booking

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(
    account_booking.router, prefix="/bookings", tags=["Bookings"]
)
