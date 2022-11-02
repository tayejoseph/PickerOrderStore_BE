from datetime import datetime
from pydantic import BaseModel, EmailStr


class CreateAccount(BaseModel):
    email: EmailStr
    password: str
    fullName: str
    phoneNum: str

class CreateAccountOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True