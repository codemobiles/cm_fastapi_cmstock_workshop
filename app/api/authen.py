from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.api import schema
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.User import User as UserDB
from app.api import security
from datetime import datetime, timedelta
from app.config.setting import settings
router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}


@router.post("/register")
def register(user: schema.User, db: Session = Depends(get_db)):

    try:
        user_db = UserDB(username=user.username,
                         password=security.get_password_hash(user.password))
        db.add(user_db)
        db.commit()
        return {"result": "ok"}
    except Exception as e:
        return {"result": "nok", "error": "duplicate username"}


@router.post("/login")
def login(user: schema.User, db: Session = Depends(get_db)):
    try:
        user_db = db.query(UserDB).filter(
            UserDB.username == user.username).first()

        # verify username
        if not user_db:
            return {"result": "nok", "error": "invalide username"}

        # verify password
        if not security.verify_password(user.password, user_db.password):
            return {"result": "nok", "error": "invalide password"}

        # create jwt token
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = security.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires)

        # login success
        return {"result": "ok", "token": token}
    except Exception as e:
        return {"result": "nok", "error": e}
