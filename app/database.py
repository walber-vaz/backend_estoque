from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
    connect_args={'check_same_thread': False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def db_init():
    Base.metadata.create_all(bind=engine)


def db_close():
    engine.dispose()


def get_session() -> Session:  # type: ignore
    with SessionLocal() as session:
        yield session
