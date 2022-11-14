from typing import Optional
from pydantic import BaseModel,EmailStr

class Token(BaseModel):
    token_type: str
    access_token: str

class StudentBase(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    is_active: Optional[bool] = True
    teacher_id: Optional[int] = None
    id: int

class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    id: int

#properties required during user creation
class UserCreate(UserBase):
    username: str
    email : EmailStr
    password : str

class TeacherCreate(BaseModel):
    firstname: str
    lastname: str
    school: str

class StudentCreate(StudentBase):
    firstname: str
    lastname: str
    is_active: bool
    teacher_id: int
    # id:int


class ShowStudent(StudentBase):
    firstname: str
    lastname: str
    is_active: bool
    teacher_id: int
    id: int

    class Config():
        orm_mode = True

class ShowUser(UserBase):
    username: Optional[str]
    email : Optional[EmailStr]
    id:int

    class Config():
        orm_mode = True
