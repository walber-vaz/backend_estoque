from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    hashed_password: str
    email: EmailStr
    is_active: bool = True


class UserWithoutPassword(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserSchemaCreate(UserBase):
    pass


class UserSchemaUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    hashed_password: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = True


class UserSchemaResponse(BaseModel):
    message: str
    data: list[UserWithoutPassword]
    status: int


class UserSchemaResponseGet(BaseModel):
    message: str
    data: list[UserWithoutPassword]
    status: int


class UserSchemaResponseUpdate(BaseModel):
    message: str
    data: list[UserSchemaUpdate] | None
    status: int


class UserId(BaseModel):
    user_id: UUID


class UserSchemaResponseCreate(BaseModel):
    message: str
    data: list[UserId]
    status: int
