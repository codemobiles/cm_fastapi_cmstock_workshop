from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class User(BaseModel):
    username: str
    password: str
    level: Optional[str] = "normal"


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


@router.post("/register")
def register(user: User):
    return user
