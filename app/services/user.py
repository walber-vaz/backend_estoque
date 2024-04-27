from http import HTTPStatus
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import (
    UserSchemaCreate,
    UserSchemaResponseCreate,
    UserSchemaResponseGetID,
)


def create_user(session: Session, user: UserSchemaCreate) -> UserSchemaResponseCreate:
    is_email_exists = session.scalar(select(User).where(User.email == user.email))

    if is_email_exists:
        raise ValueError('Email already exists')

    new_user = User(
        email=user.email,
        hashed_password=user.hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    response = UserSchemaResponseCreate(
        message='User created successfully', status=HTTPStatus.CREATED, data=new_user.id
    )

    return response


def get_user_by_id(session: Session, user_id: UUID) -> UserSchemaResponseGetID:
    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise ValueError('User not found')

    return user
