from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship
from app.db.base import Base


class Address(Base):
    __tablename__ = "addresses"


    id = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    city = mapped_column(String)
    state = mapped_column(String)
    country = mapped_column(String)


    user = relationship("User", back_populates="addresses")