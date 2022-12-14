from fastapi import APIRouter

from apis.v1 import users_route, student_route, auth_route

base_router = APIRouter()

base_router.include_router(users_route.router, prefix="/users", tags=["users"])
base_router.include_router(student_route.router, prefix="/students", tags=["students"])
base_router.include_router(auth_route.router, prefix="/auth", tags=["auth"])


