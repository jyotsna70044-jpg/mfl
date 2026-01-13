from pydantic import BaseModel, validator
from datetime import date, datetime


class PaymentCreate(BaseModel):
    loan_id: int
    amount: float
    payment_date: date
    idempotency_key: str

    @validator("payment_date", pre=True)
    def parse_indian_date(cls, v):
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Date must be DD/MM/YYYY")
        return v


class PaymentRead(BaseModel):
    id: int
    amount: float
    payment_date: date

    model_config = {"from_attributes": True}
