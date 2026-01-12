from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.loan import LoanCreate, LoanRead
from models.loan import Loan
from services.emi import calculate_emi
from db.session import AsyncSessionLocal

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post("", response_model=LoanRead)
async def create_loan(user_id: int, payload: LoanCreate):
    async with AsyncSessionLocal() as db:
        print(payload)
        print(user_id)
        # emi = calculate_emi(payload.principal, payload.interest_rate, payload.tenure_months)
        emi = 5000
        loan = Loan(user_id=user_id, emi=emi, **payload.model_dump())
        db.add(loan)
        await db.commit()
        await db.refresh(loan)
        return loan
