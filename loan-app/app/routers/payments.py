from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.payment import PaymentCreate, PaymentRead
from app.services.payment_service import get_or_create_payment
from app.db.session import AsyncSessionLocal

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("", response_model=PaymentRead)
async def pay(payload: PaymentCreate):
    async with AsyncSessionLocal() as db:
        return await get_or_create_payment(db, payload)
