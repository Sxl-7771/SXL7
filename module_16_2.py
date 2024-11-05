from fastapi import FastAPI, Path
from pydantic import PositiveInt
from typing import Annotated

app = FastAPI()


@app.get("12.0.0.1:8000")
async def read_root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples={"example1": 1})]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples={"example1": "UrbanUser"})],
    age: Annotated[PositiveInt, Path(title="Enter age", ge=18, le=120, examples={"example1": 24})],
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
