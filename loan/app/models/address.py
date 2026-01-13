from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True
    )
    muhalla: Mapped[str] = mapped_column(String)
    ward_no: Mapped[str] = mapped_column(String)
    village: Mapped[str] = mapped_column(String)

    post_office: Mapped[str] = mapped_column(String)
    police_station: Mapped[str] = mapped_column(String)
    postal_code: Mapped[str] = mapped_column(String)

    district: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="addresses"
    )
