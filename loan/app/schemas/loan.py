from pydantic import BaseModel, Field


class LoanCreate(BaseModel):
    principal: float = Field(gt=0)
    interest_rate: float = Field(gt=0)
    tenure_months: int = Field(gt=0)


class LoanRead(BaseModel):
    id: int
    principal: float
    interest_rate: float
    tenure_months: int
    emi: float
    status: str

    model_config = {"from_attributes": True}
