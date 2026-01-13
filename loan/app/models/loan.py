from sqlalchemy import ForeignKey, Float, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from db.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True
    )

    principal: Mapped[float]
    interest_rate: Mapped[float]
    tenure_months: Mapped[int]
    emi: Mapped[float]

    status: Mapped[str] = mapped_column(default="ACTIVE")

    # 👇 USER RELATIONSHIP (ADDED)
    user: Mapped["User"] = relationship(
        "User",
        back_populates="loans"
    )

    payments: Mapped[List["Payment"]] = relationship(
        "Payment",
        back_populates="loan",
        cascade="all, delete-orphan"
    )
