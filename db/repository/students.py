from db.models import Student
from schemas import StudentCreate
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import Depends




def create_new_student(student:StudentCreate, db:Session):
    new_student  = Student(
        firstname = student.firstname,
        lastname=student.lastname,
        teacher_id=1,
        is_active = True
    )
    print("Adding new student")
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def retrieve_student(id:int, db:Session):
    student =  db.query(Student).filter(Student.id ==id).first()
    return student