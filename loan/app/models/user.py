from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    mobile: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(String)

    role: Mapped[str] = mapped_column(
        String,
        default="USER"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    addresses: Mapped[List["Address"]] = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    loans: Mapped[List["Loan"]] = relationship(
        "Loan",
        back_populates="user",
        cascade="all, delete-orphan"
    )
