from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.api import schema
router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


def d1():
    return "Hey"


@router.post("/register")
def register(user: schema.User, msg: str = Depends(d1)):
    print("Register is called" + msg)
    return user


@router.post("/login")
def login(user: schema.User):
    return user
