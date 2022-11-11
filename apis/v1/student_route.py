from fastapi import APIRouter,  Depends, Response
from db.models import Student
from sqlalchemy.orm import Session
from schemas import StudentCreate
from db.session import get_db
from db.repository.students import create_new_student

router = APIRouter()

@router.post("/")
def create_student(student:StudentCreate, db:Session=Depends(get_db)):
    student = create_new_student(student=student, db=db)
    return Response("student created", status_code=200)

@router.get("/")
def get_students(db:Session=Depends(get_db)):
    return{
        "Ehyaa"
    }
