from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "tg_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str | None]
    city: Mapped[str | None]
    language: Mapped[str | None]
    state: Mapped[str | None]
    phone: Mapped[str | None]

    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("tg_users.id"))
    telegram_payment_id: Mapped[str]
    amount: Mapped[int]
    currency: Mapped[str]
    status: Mapped[str] = mapped_column(default="paid")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user = relationship("User", back_populates="orders")