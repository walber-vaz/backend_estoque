from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_session
from app.schemas.auth import Token
from app.services.auth import authenticate_user

router = APIRouter(tags=['auth'])


@router.post('/login', response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
) -> Token:
    try:
        response = authenticate_user(session=session, form_data=form_data)
        return response
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail=str(e))
