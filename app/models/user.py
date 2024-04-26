from datetime import datetime
from uuid import UUID

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column
from zoneinfo import ZoneInfo

from app.database import reg


@reg.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text('gen_random_uuid()'), init=False
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    email: Mapped[str] = mapped_column(
        String(200), nullable=False, unique=True, index=True
    )
    password: Mapped[str] = mapped_column(String(24), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(tz=ZoneInfo('UTC')), init=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(tz=ZoneInfo('UTC')),
        onupdate=datetime.now(tz=ZoneInfo('UTC')),
        init=False,
    )
