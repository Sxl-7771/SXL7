from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import User as UserModel
from schemas import User
from backend.db_depends import get_db

app = FastAPI()
router = APIRouter()


@router.get("/", response_model=List[User])
async def all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_data = User(**user.dict(), slug=slugify(user.username))
    db.execute(insert(User).values(user_data))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    db_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    db.execute(delete(User).where(User.id == user_id))
    db.commit()


@router.get("/{user_id}/tasks", response_model=List[TaskModel])
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user_id).all()
    return tasks


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.query(TaskModel).filter(TaskModel.user_id == user_id).delete()
    db.delete(db_user)
    db.commit()
