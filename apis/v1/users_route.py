from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user, retrieve_user



router =  APIRouter()


@router.post("/create_user/")
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    user = create_new_user(user=user, db=db)

@router.get("/get_user/{id}/", response_model=ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    user = retrieve_user(id=id, db=db)
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with ID {id} not found")


