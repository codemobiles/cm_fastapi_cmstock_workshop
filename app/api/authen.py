from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.api import schema
from app.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


@router.post("/register")
def register(user: schema.User, db: Session = Depends(get_db)):
    print("Register is called" + msg)
    return user


@router.post("/login")
def login(user: schema.User):
    return user
