from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import registry

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)


reg = registry()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(reg.metadata.create_all(engine))


async def close_db():
    await engine.sync_engine.dispose()


async def get_session():
    async_session = async_sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
