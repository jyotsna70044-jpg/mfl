from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.loan import LoanCreate, LoanRead
from app.models.loan import Loan
from app.services.emi import calculate_emi
from app.db.session import AsyncSessionLocal

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post("", response_model=LoanRead)
async def create_loan(user_id: int, payload: LoanCreate):
    async with AsyncSessionLocal() as db:
        emi = calculate_emi(payload.principal, payload.rate, payload.tenure_months)
        loan = Loan(user_id=user_id, emi=emi, **payload.model_dump())
        db.add(loan)
        await db.commit()
        await db.refresh(loan)
        return loan
