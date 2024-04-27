from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.schemas.user import UserSchemaCreate, UserSchemaResponseCreate
from app.services.user import create_user

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
