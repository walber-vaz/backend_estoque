from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import database


@asynccontextmanager
async def lifecycle(app: FastAPI):
    try:
        await database.init_db()
        yield
    finally:
        await database.close_db()


app = FastAPI(lifespan=lifecycle)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
