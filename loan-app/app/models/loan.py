from sqlalchemy import ForeignKey, Numeric, Integer, Float, String
from sqlalchemy.orm import mapped_column, relationship
from app.db.base import Base


class Loan(Base):
    __tablename__ = "loans"


    id = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    principal = mapped_column(Numeric(12,2))
    rate = mapped_column(Float)
    tenure_months = mapped_column(Integer)
    emi = mapped_column(Numeric(12,2))
    status = mapped_column(String, default="ACTIVE")


    user = relationship("User", back_populates="loans")
    payments = relationship("Payment", back_populates="loan")