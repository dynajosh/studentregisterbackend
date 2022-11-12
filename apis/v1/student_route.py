from fastapi import APIRouter,  Depends, Response, HTTPException, status
from db.models import Student
from sqlalchemy.orm import Session
from schemas import StudentCreate, ShowStudent
from db.session import get_db
from db.repository.students import create_new_student, retrieve_student

router = APIRouter()

@router.post("/create_student")
def create_student(student:StudentCreate, db:Session=Depends(get_db)):
    student = create_new_student(student=student, db=db)
    return Response("student created", status_code=200)

@router.get("/get_student/{id}", response_model=ShowStudent)
def get_student(id:int, db:Session=Depends(get_db)):
    student = retrieve_student(id=id, db=db)
    if not student:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Student with this id {id} does not exist")
    
