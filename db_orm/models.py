from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

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