from fastapi import APIRouter, Form, Depends
from pydantic import BaseModel
from typing import Optional
from app.api import schema

from app.db import get_db
from sqlalchemy.orm import Session
from app.models.User import User as UserDB
from app.api import security


router = APIRouter()


@router.get("/")
def get_product():
    return [1, 2, 3]


def get_product_form(id: Optional[str] = Form(None),
                     name: str = Form(...),
                     price: float = Form(...),
                     stock: int = Form(...)):
    return schema.Product(id=id, name=name, price=price, stock=stock, image="")


@router.post("/")
async def insert_product(product: schema.Product = Depends(get_product_form),
                         db: Session = Depends(get_db)):
    return product


@router.get("/{id}")
def get_product_by_id(id: str):
    return {"id": id}
