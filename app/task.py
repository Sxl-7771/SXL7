from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models import Task as TaskModel, User as UserModel
from schemas import CreateTask, UpdateTask
from backend.db_depends import get_db

app = FastAPI()
router = APIRouter()


@router.get("/", response_model=List[TaskModel])
async def all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return tasks


@router.get("/{task_id}", response_model=TaskModel)
async def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    task_data = TaskModel(**task.dict(), user_id=user_id)
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: UpdateTask, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.delete(db_task)
    db.commit()
