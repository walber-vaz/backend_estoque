from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    hashed_password: str
    email: EmailStr
    is_active: bool = True


class UserSchemaCreate(UserBase):
    model_config = ConfigDict(from_attributes=True)


class UserSchemaResponseCreate(BaseModel):
    message: str
    data: UUID
    status: int
