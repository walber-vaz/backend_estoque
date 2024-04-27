from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


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


class UserSchemaResponseGetID(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    hashed_password: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
