from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import db_close, db_init
from app.routers.user import router as user_router


@asynccontextmanager
async def get_session(app: FastAPI):
    await db_init()
    yield
    await db_close()


app = FastAPI(lifespan=get_session)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_router, prefix=settings.PREFIX)


@app.get(f'{settings.PREFIX}/health')
async def health():
    return {'status': 'ok'}
