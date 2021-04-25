from fastapi import APIRouter, Form, Depends, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from app.api import schema

from app.db import get_db
from sqlalchemy.orm import Session
from app.models.Product import Product as ProductDB
from app.api import security
from pathlib import Path
import os

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
                         image: UploadFile = File(...),
                         db: Session = Depends(get_db)):
    try:
        db_product = ProductDB(**product.dict())
        db.add(db_product)
        db.commit()
        return {"result": "ok", "image": image}
    except Exception as e:
        return {"product": "nok", "error": str(e)}


@router.get("/{id}")
def get_product_by_id(id: str):
    return {"id": id}
