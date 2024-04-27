from http import HTTPStatus

from app.config import settings


def test_read_main(client):
    response = client.get(f'{settings.PREFIX}/health')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'status': 'ok'}
