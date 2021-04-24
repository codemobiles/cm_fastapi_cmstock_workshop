from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.api import schema
router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


@router.post("/register")
def register(user: schema.User):
    return user


@router.post("/login")
def login(user: schema.User):
    return user
