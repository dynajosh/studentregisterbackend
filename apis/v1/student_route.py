from fastapi import APIRouter,  Depends, Response, HTTPException, status
from db.models import Student
from sqlalchemy.orm import Session
from schemas import StudentCreate, ShowStudent
from db.session import get_db
from db.repository.students import create_new_student, retrieve_student, fetch_all_students, update_student_data, delete_a_student
from typing import List

router = APIRouter()

@router.post("/create")
def create_student(student:StudentCreate, db:Session=Depends(get_db)):
    student = create_new_student(student=student, db=db)
    return Response("student created", status_code=200)

@router.get("/get/{id}/", response_model=ShowStudent)
def get_student(id:int, db:Session=Depends(get_db)):
    student = retrieve_student(id=id, db=db)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with this id {id} does not exist")
    
@router.get("/get-all/", response_model=List[ShowStudent])
def get_all_students(db:Session=Depends(get_db)):
    students = fetch_all_students(db=db)
    return students

@router.put("/update/{id}/", response_model=StudentCreate)
def update_student(id:int, student:StudentCreate, db:Session=Depends(get_db)):
    current_user = 1
    message = update_student_data(id=id, db=db, student=student)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")
    else:
        return {"msg":"Successfully updated."}

@router.delete("delete/{id}")
def delete_student(id:int, db:Session=Depends(get_db)):
    current_user = 1
    student = delete_a_student(id=id, db=db, teacher_id=current_user)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")
    else:
        return {"msg":"Successfully deleted."}
