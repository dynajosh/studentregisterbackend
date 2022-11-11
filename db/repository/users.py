from db.models import User
from core.hashing import Hasher
from schemas import UserCreate
from sqlalchemy.orm import Session

def create_new_user(user:UserCreate, db:Session):
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password = Hasher.get_password_hash(user.password),
        is_active = True,
    )
    print("new user creating")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
