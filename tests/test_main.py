from http import HTTPStatus

import pytest

from app.config import settings


@pytest.mark.asyncio()
async def test_read_main(client):
    response = await client.get(f'{settings.PREFIX}/health')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'status': 'ok'}
