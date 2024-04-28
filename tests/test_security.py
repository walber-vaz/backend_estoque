from app.security import create_access_token, decode_token


def test_jwt():
    data = {'sub': 'test'}
    token = create_access_token(data)

    decoded = decode_token(token)

    assert decoded['sub'] == data['sub']
    assert 'exp' in decoded
