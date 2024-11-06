from fastapi import FastAPI, Path, HTTPException
from pydantic import PositiveInt, BaseModel
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
next_user_id = 2


class User(BaseModel):
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)]
    age: Annotated[PositiveInt, Path(title="Enter age", ge=18, le=120)]


@app.get("/users")
async def read_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int):
    global next_user_id
    if not 5 <= len(username) <= 20 or not 18 <= age <= 120:
        raise HTTPException(status_code=422, detail="Invalid username or age")
    users[str(next_user_id)] = f"Имя: {username}, возраст: {age}"
    message = f"User {next_user_id} is registered"
    next_user_id += 1
    return message


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if not 5 <= len(username) <= 20 or not 18 <= age <= 120:
        raise HTTPException(status_code=422, detail="Invalid username or age")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"

