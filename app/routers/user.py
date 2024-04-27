from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.user import UserSchemaCreate, UserSchemaResponseCreate
from app.services.user import create_user

router = APIRouter(tags=['user'])


@router.post(
    '/users', status_code=HTTPStatus.CREATED, response_model=UserSchemaResponseCreate
)
async def create(
    user: UserSchemaCreate, session: AsyncSession = Depends(get_session)
) -> UserSchemaResponseCreate | Exception:
    try:
        response = await create_user(session=session, user=user)
        return response
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
