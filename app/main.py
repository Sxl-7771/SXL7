from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.backend.db import Base, engine
from app.models.task import Task
from app.models.user import User


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

print("SQL для User:")
print(User.__table__.compile(compile_kwargs={"literal_binds": True}))

print("\nSQL для Task:")
print(Task.__table__.compile(compile_kwargs={"literal_binds": True}))

