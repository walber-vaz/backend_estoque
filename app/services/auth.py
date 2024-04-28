from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import Token
from app.security import create_access_token, refresh_access_token, verify_password


def authenticate_user(session: Session, form_data: OAuth2PasswordRequestForm) -> Token:
    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise ValueError('Incorrect email or password')

    if not verify_password(form_data.password, user.hashed_password):
        raise ValueError('Incorrect email or password')

    access_token = create_access_token(data={'sub': str(user.id)})
    refresh_token = refresh_access_token(data={'sub': str(user.id)})

    response = Token(
        access_token=access_token, refresh_token=refresh_token, token_type='bearer'
    )

    return response
