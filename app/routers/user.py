from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.schemas.user import (
    UserSchemaCreate,
    UserSchemaResponseCreate,
    UserSchemaResponseGet,
    UserSchemaResponseUpdate,
    UserSchemaUpdate,
)
from app.services.user import create_user, get_user_by_id, update_user_by_id

router = APIRouter(tags=['user'])


@router.post(
    '/users', status_code=HTTPStatus.CREATED, response_model=UserSchemaResponseCreate
)
def create(
    user: UserSchemaCreate, session: Session = Depends(get_session)
) -> UserSchemaResponseCreate | Exception:
    try:
        response = create_user(session=session, user=user)
        return response
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get(
    '/users/{user_id}', response_model=UserSchemaResponseGet, status_code=HTTPStatus.OK
)
def get_by_id(
    user_id: UUID, session: Session = Depends(get_session)
) -> UserSchemaResponseGet | Exception:
    try:
        response = get_user_by_id(session=session, user_id=user_id)
        return response
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))


@router.put(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserSchemaResponseUpdate,
    response_model_exclude_none=True,
)
def update_by_id(
    data: UserSchemaUpdate, user_id: UUID, session: Session = Depends(get_session)
) -> UserSchemaResponseUpdate | Exception:
    try:
        response = update_user_by_id(data=data, session=session, user_id=user_id)
        return response
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))
