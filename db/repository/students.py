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
    student =  db.query(Student).filter(Student.id == id)
    return student

def fetch_all_students(db:Session):
    students = db.query(Student).all()
    # for i in students:
    #     print(i.firstname, i.lastname, i.teacher_id)
    return students

def update_student_data(id:int, student:StudentCreate, db:Session):
    existing_student = db.query(Student).filter(id==id)
    if not existing_student.first():
        return 0

    # student.__dict__.update(teacher_id=teacher_id)
    existing_student.update(student.__dict__)
    db.commit()
    return 1

def delete_a_student(id:int, db:Session, teacher_id:int):
    existing_student = db.query(Student).filter(Student.id==id)
    existing_student.delete(synchronize_session=False)
    db.commit()
    return 1

