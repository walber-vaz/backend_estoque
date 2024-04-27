from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    hashed_password: str
    email: EmailStr
    is_active: bool = True


class UserSchemaCreate(UserBase):
    pass


class UserSchemaResponseCreate(BaseModel):
    message: str
    data: UUID
    status: int
