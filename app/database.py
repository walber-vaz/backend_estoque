from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True, future=True)


class Base(DeclarativeBase):
    pass


def db_init():
    Base.metadata.create_all


def db_close():
    engine.dispose()


def get_session():
    session = sessionmaker(
        bind=engine, future=True, autocommit=False, expire_on_commit=False
    )
    with session() as session:
        yield session
