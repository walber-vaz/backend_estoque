from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False, index=True, unique=True
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now, index=True, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now,
        index=True,
        server_default=func.now(),
        onupdate=datetime.now,
    )
