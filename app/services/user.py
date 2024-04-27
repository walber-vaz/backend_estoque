from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserSchemaResponseCreate


async def create_user(session: AsyncSession, user: User) -> UserSchemaResponseCreate:
    """
    Creates a new user in the database.

    Args:
        session (AsyncSession): The async session to use for the database transaction.
        user (User): The user object containing the user details.

    Returns:
        UserSchemaResponseCreate:
            The response object containing the result of the user creation.

    Raises:
        None

    Example:
        >>> session = AsyncSession()
        >>> user = User(email='example@example.com', hashed_password='hashed_password')
        >>> create_user(session, user)
        UserSchemaResponseCreate(
            message='User created successfully',
            status=HTTPStatus.CREATED,
            data=user.id
        )
    """
    is_email_exists = await session.scalar(select(User).where(User.email == user.email))

    if is_email_exists:
        response = UserSchemaResponseCreate(
            message='Email already exists', status=HTTPStatus.CONFLICT, data=None
        )
        return response

    session.add(user)
    await session.commit()
    await session.refresh(user)

    response = UserSchemaResponseCreate(
        message='User created successfully', status=HTTPStatus.CREATED, data=user.id
    )
    return response
