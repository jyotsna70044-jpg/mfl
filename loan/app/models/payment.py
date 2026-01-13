from datetime import date
from sqlalchemy import ForeignKey, Float, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)

    loan_id: Mapped[int] = mapped_column(ForeignKey("loans.id"))
    amount: Mapped[float]

    payment_date: Mapped[date] = mapped_column(Date)
    idempotency_key: Mapped[str] = mapped_column(unique=True)

    loan: Mapped["Loan"] = relationship(
        "Loan",
        back_populates="payments"
    )


