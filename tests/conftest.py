import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.database import Base, get_session
from app.main import app
from app.models.user import User


@pytest.fixture()
def session():
    engine = create_engine(settings.DATABASE_URI_TEST)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    with session() as session:
        yield session
        session.rollback()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def user(session):
    user = User(
        first_name='John',
        last_name='Doe',
        hashed_password='password',
        email='john_done@email.com',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
