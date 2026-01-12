from pydantic import BaseModel
from datetime import date


class PaymentCreate(BaseModel):
    loan_id: int
    amount: float
    payment_date: date
    idempotency_key: str


class PaymentRead(BaseModel):
    id: int
    amount: float
    payment_date: date

    model_config = {"from_attributes": True}
