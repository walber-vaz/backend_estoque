from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        index=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        nullable=False,
        default=uuid4,
    )
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(24))
    is_active: Mapped[bool] = mapped_column(default=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False, default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        nullable=False,
        default=datetime.now,
        server_default=func.now(),
    )
