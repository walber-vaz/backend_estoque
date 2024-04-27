from http import HTTPStatus

import pytest
from pydantic import ValidationError

from app.schemas.user import UserSchemaCreate
from app.services.user import create_user


def test_create_user_success(session):
    # Arrange
    user_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'hashed_password': 'hashed_password',
        'email': 'john@gmail.com',
    }
    user_schema = UserSchemaCreate(**user_data)

    response = create_user(session, user_schema)

    assert response.status == HTTPStatus.CREATED
    assert response.message == 'User created successfully'


def test_create_user_duplicate_email(session):
    user_data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'hashed_password': 'hashed_password',
        'email': 'jane@gmail.com',
    }
    user_schema = UserSchemaCreate(**user_data)
    create_user(session, user_schema)

    with pytest.raises(ValueError, match='Email already exists'):
        create_user(session, user_schema)


def test_create_user_invalid_email(session):
    invalid_user_data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'hashed_password': 'hashed_password',
        'email': 'janegmail.com',
    }

    with pytest.raises(ValidationError):
        UserSchemaCreate(**invalid_user_data)
