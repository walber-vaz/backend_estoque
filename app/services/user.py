from http import HTTPStatus
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import (
    UserSchemaCreate,
    UserSchemaResponseCreate,
    UserSchemaResponseGet,
    UserSchemaResponseUpdate,
    UserSchemaUpdate,
    UserWithoutPassword,
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
        message='User created successfully',
        status=HTTPStatus.CREATED,
        data=[{'user_id': new_user.id}],
    )

    return response


def get_user_by_id(session: Session, user_id: UUID) -> UserSchemaResponseGet:
    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise ValueError('User not found')

    response = UserSchemaResponseGet(
        message='User found successfully',
        status=HTTPStatus.OK,
        data=[UserWithoutPassword(**user.__dict__)],
    )

    return response


def update_user_by_id(data: UserSchemaUpdate, session: Session, user_id: UUID):
    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise ValueError('User not found')

    update_fields = {}
    for key, value in data.model_dump(exclude_none=True).items():
        if getattr(user, key) != value:
            setattr(user, key, value)
            update_fields[key] = value

    session.commit()
    session.refresh(user)

    response = UserSchemaResponseUpdate(
        message='User updated successfully', status=HTTPStatus.OK, data=[update_fields]
    )

    return response


def delete_user_by_id(session: Session, user_id: UUID):
    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise ValueError('User not found')

    user.is_active = False
    session.commit()

    response = UserSchemaResponseUpdate(
        message='User deleted successfully', status=HTTPStatus.NO_CONTENT, data=None
    )

    return response
