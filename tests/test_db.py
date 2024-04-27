from sqlalchemy import select

from app.models.user import User


def test_create_user(session, user):
    new_user = session.scalar(select(User).where(User.email == user.email))

    assert new_user.first_name == user.first_name
    assert new_user.last_name == user.last_name
    assert new_user.email == user.email
    assert new_user.hashed_password == user.hashed_password
    assert new_user.is_active is True
    assert new_user.created_at is not None
    assert new_user.updated_at is not None
