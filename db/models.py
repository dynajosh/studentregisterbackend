from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base


class Student(Base):
    id = Column(Integer, index=True, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    # teacher = relationship("Teacher",back_populates="students")


class Teacher(Base):
    id = Column(Integer, index=True, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    school = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))


class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
