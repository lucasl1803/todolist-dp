from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
import models
from routers import task_router, category_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router.router)
app.include_router(task_router.router)


@app.get("/")
def read_root():
    return {"message": "To-Do List rodando CRUD completo :)"}
