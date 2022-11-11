from typing import Optional
from pydantic import BaseModel,EmailStr


#properties required during user creation
class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str

class TeacherCreate(BaseModel):
    firstname: str
    lastname: str
    school: str

class StudentCreate(BaseModel):
    firstname: str
    lastname: str
    is_active: bool
    teacher: int