from http import HTTPStatus

from app.config import settings


def test_get_token(client, user):
    response = client.post(
        f'{settings.PREFIX}/login',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token.get('access_token') is not None
    assert token.get('refresh_token') is not None
    assert token.get('token_type') == 'bearer'


def test_get_token_incorrect_email(client, user):
    response = client.post(
        f'{settings.PREFIX}/login',
        data={'username': 'incorrect@email.com', 'password': user.clean_password},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json().get('detail') == 'Incorrect email or password'


def test_get_token_incorrect_password(client, user):
    response = client.post(
        f'{settings.PREFIX}/login',
        data={'username': user.email, 'password': 'incorrect_password'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json().get('detail') == 'Incorrect email or password'
