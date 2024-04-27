from http import HTTPStatus

from app.config import settings


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
