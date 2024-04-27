from http import HTTPStatus

from app.config import settings
from app.schemas.user import UserSchemaResponseGetID


def test_helth_check(client):
    response = client.get(f'{settings.PREFIX}/health')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'status': 'ok'}


def test_create_user(client):
    response = client.post(
        f'{settings.PREFIX}/users',
        json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john_done@email.com',
            'hashed_password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'message': 'User created successfully',
        'status': HTTPStatus.CREATED,
        'data': response.json().get('data'),
    }


def test_create_user_email_exists(client, user):
    response = client.post(
        f'{settings.PREFIX}/users',
        json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': user.email,
            'hashed_password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists'}


def test_get_user_by_id(client, user):
    user_validate = UserSchemaResponseGetID.model_validate(user).model_dump(mode='json')

    response = client.get(f'{settings.PREFIX}/users/{user_validate.get("id")}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_validate


def test_get_user_by_id_not_found(client):
    response = client.get(
        f'{settings.PREFIX}/users/12345678-1234-5678-1234-567812345678'
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
