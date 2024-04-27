from sqlalchemy import select

from app.models.user import User


def test_create_user(session):
    new_user = User(
        first_name='John',
        last_name='Doe',
        email='john_doe@email.com',
        hashed_password='password',
    )

    session.add(new_user)
    session.commit()

    stmt = session.scalar(select(User).where(User.email == 'john_doe@email.com'))

    assert stmt.email == 'john_doe@email.com'
    assert stmt.first_name == 'John'
    assert stmt.last_name == 'Doe'
    assert stmt.hashed_password == 'password'
    assert stmt.is_active is True
    assert stmt.created_at is not None
    assert stmt.updated_at is not None
