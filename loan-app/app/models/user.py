from sqlalchemy import String, Boolean
from sqlalchemy.orm import mapped_column, relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"


    id = mapped_column(primary_key=True)
    email = mapped_column(String, unique=True, index=True)
    hashed_password = mapped_column(String)
    role = mapped_column(String, default="USER")
    is_active = mapped_column(Boolean, default=True)


    addresses = relationship("Address", back_populates="user")
    loans = relationship("Loan", back_populates="user")