import datetime
from typing import Optional
from fastapi import APIRouter, Depends, File, Form, UploadFile
from app.api import security
from app.models.Transaction import Transaction as TransactionDB
from app.db import get_db
from sqlalchemy import desc
from sqlalchemy.orm import Session
from app.api import schema
import shutil
from pathlib import Path
import os

router = APIRouter()


@router.get("/")
def get_transaction():
    return {"result": "transaction"}


@router.post("/")
def insert_transaction(transaction: schema.Transaction,
                       db: Session = Depends(get_db)):
    try:
        db_transaction = TransactionDB(**transaction.dict())
        db.add(db_transaction)
        db.commit()
        return db_transaction.as_dict()
    except Exception as e:
        return {"transaction": "nok", "error": str(e)}
