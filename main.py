from fastapi import FastAPI

from database import Base, engine
import models
from routers import task_router, category_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List")

app.include_router(category_router.router)
app.include_router(task_router.router)


@app.get("/")
def read_root():
    return {"message": "To-Do List  rodando com CRUD completo :)"}
