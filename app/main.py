from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import db_close, db_init


@asynccontextmanager
async def get_session():
    db_init()
    yield
    db_close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get(f'{settings.PREFIX}/health')
def health():
    return {'status': 'ok'}
