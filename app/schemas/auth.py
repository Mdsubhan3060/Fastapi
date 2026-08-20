from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    email: str
    password: str
class UserLogin(BaseModel):
    email: str
    password: str
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role:str
class RefreshTokenRequest(BaseModel):
    refresh_token: str
class AdminUserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str