from http import HTTPStatus


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    user = {
        'username': 'test_username',
        'email': 'email@email.com',
        'full_name': 'Test User',
        'password': 'password',
    }

    response = client.post('/users', json=user)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test_username',
        'email': 'email@email.com',
        'full_name': 'Test User',
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'test_username',
                'email': 'email@email.com',
                'full_name': 'Test User',
            }
        ]
    }


def test_update_user(client):
    user = {'username': 'test_username 2'}

    response = client.put('/users/1', json=user)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'message': 'User updated successfully',
        'status': HTTPStatus.OK,
    }


def test_update_user_not_found(client):
    user = {'username': 'test_username 2'}

    response = client.put('/users/2', json=user)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted successfully',
        'status': HTTPStatus.OK,
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
