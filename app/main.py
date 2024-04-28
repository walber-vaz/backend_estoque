from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from app.schemas import (
    Message,
    UserSchemaAllUsers,
    UserSchemaCreate,
    UserSchemaDB,
    UserSchemaResponse,
    UserSchemaResponseMessage,
    UserSchemaResponseUpdate,
    UserSchemaUpdate,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def hello_world():
    return {'message': 'Hello, World!'}


@app.post(
    '/users',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaResponse,
    response_model_exclude_none=True,
)
def create_user(user: UserSchemaCreate) -> UserSchemaDB:
    user_with_id = UserSchemaDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserSchemaAllUsers)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserSchemaResponseUpdate,
    response_model_exclude_none=True,
)
def update_user(user_id: int, user: UserSchemaUpdate) -> UserSchemaResponseUpdate:
    if user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    for key, value in user.model_dump(exclude_none=True).items():
        if value is not None:
            setattr(database[user_id - 1], key, value)

    response = UserSchemaResponseUpdate(
        id=user_id, message='User updated successfully', status=HTTPStatus.OK
    )

    return response


@app.delete('/users/{user_id}')
def delete_user(user_id: int) -> UserSchemaResponseMessage:
    if user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    del database[user_id - 1]

    response = UserSchemaResponseMessage(
        message='User deleted successfully', status=HTTPStatus.OK
    )

    return response
