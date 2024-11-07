from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

users = []


class User(BaseModel):
    id: int = Field(..., ge=1)
    username: str = Field(..., min_length=5, max_length=20)
    age: int = Field(..., ge=18, le=120)


@app.get("/users")
async def read_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int):
    next_id = 1 if not users else users[-1].id + 1
    new_user = User(id=next_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = User(id=user_id, username=username, age=age)
            return users[i]
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")

