from sqlalchemy import ForeignKey, Numeric, Integer, Float, String
from sqlalchemy.orm import mapped_column, relationship


from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    principal: Mapped[float] = mapped_column(Float, nullable=False)
    interest_rate: Mapped[float] = mapped_column(Float, nullable=False)
    tenure_months: Mapped[int] = mapped_column(Integer, nullable=False)
    emi = mapped_column(Numeric(12, 2))
    status: Mapped[str] = mapped_column(String, default="ACTIVE")



# class Loan(Base):
#     __tablename__ = "loans"
#
#
#     id = mapped_column(primary_key=True)
#     user_id = mapped_column(ForeignKey("users.id"))
#     principal = mapped_column(Numeric(12,2))
#     rate = mapped_column(Float)
#     tenure_months = mapped_column(Integer)
#     emi = mapped_column(Numeric(12,2))
#     status = mapped_column(String, default="ACTIVE")
#
#
#     user = relationship("User", back_populates="loans")
#     payments = relationship("Payment", back_populates="loan")