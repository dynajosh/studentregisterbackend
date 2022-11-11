from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import base_router

def include_router(app):
    app.include_router(base_router)

def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app

app = start_application()

@app.get("/")
def index():
    return {
        "message" : "Hello World"}