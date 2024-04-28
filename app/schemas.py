from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    is_active: bool | None = True


class UserSchemaCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str


class UserSchemaUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    full_name: str | None = None
    password: str | None = None
    is_active: bool | None = True


class UserSchemaResponseUpdate(BaseModel):
    id: int
    message: str
    status: int


class UserSchemaResponseMessage(BaseModel):
    message: str
    status: int


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str


class UserSchemaDB(UserSchema):
    id: int


class UserSchemaAllUsers(BaseModel):
    users: list[UserSchemaResponse]
