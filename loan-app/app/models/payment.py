from sqlalchemy import ForeignKey, Numeric, String, Date
from sqlalchemy.orm import mapped_column, relationship
from app.db.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = mapped_column(primary_key=True)
    loan_id = mapped_column(ForeignKey("loans.id"))
    amount = mapped_column(Numeric(12,2))
    payment_date = mapped_column(Date)
    idempotency_key = mapped_column(String, unique=True)


    loan = relationship("Loan", back_populates="payments")