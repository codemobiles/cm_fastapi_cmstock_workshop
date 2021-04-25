from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.api import schema
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.User import User as UserDB
router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


@router.post("/register")
def register(user: schema.User, db: Session = Depends(get_db)):
    user_db = UserDB(username=user.username, password=user.password)
    db.add(user_db)
    db.commit()
    return user


@router.post("/login")
def login(user: schema.User):
    return user
