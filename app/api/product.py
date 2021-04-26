from fastapi import APIRouter, Form, Depends, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from app.api import schema
from sqlalchemy import desc
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.Product import Product as ProductDB
from app.api import security
from pathlib import Path
import os
import shutil

router = APIRouter()


@router.get("/")
def get_product(db: Session = Depends(get_db)):
    product_db = db.query(ProductDB).order_by(desc("created_at"))
    return product_db.all()


def get_product_form(id: Optional[str] = Form(None),
                     name: str = Form(...),
                     price: float = Form(...),
                     stock: int = Form(...)):
    return schema.Product(id=id, name=name, price=price, stock=stock, image="")


def save_upload_file(upload_file: UploadFile, id: str) -> str:
    try:
        fileName = "{}.jpg".format(id)
        dest = Path(os.getcwd() + "/uploaded/images/{}".format(fileName))
        with dest.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        return fileName
    finally:
        upload_file.file.close()


def delete_upload_file(fileName: str) -> None:
    filePath = os.getcwd() + "/uploaded/images/{}".format(fileName)
    if os.path.exists(filePath):
        os.remove(filePath)


@router.put("/")
async def update_product(product: schema.Product = Depends(get_product_form),
                         image: Optional[UploadFile] = File(None),
                         db: Session = Depends(get_db)):
    try:
        # update meta
        product_db = db.query(ProductDB).filter(ProductDB.id == product.id)
        product_db.update({ProductDB.name: product.name,
                           ProductDB.price: product.price,
                           ProductDB.stock: product.stock})
        db.commit()

        # Update image name in db
        if image:
            save_upload_file(image, product.id)

        return product_db.first().as_dict()
    except Exception as e:
        return {"product": "nok", "error": str(e)}


@router.delete("/{id}")
async def delete_product(id: str, db: Session = Depends(get_db)):
    try:
        products = db.query(ProductDB).filter(ProductDB.id == id)
        imageFile = products.first().image

        delete_upload_file(imageFile)
        products.delete()
        db.commit()
        return {"result": "ok"}
    except Exception as e:
        return {"product": "nok", "error": str(e)}


@router.get("/{id}")
async def get_product_by_id(id: str, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == id).first()
    return product


@router.post("/")
async def insert_product(product: schema.Product = Depends(get_product_form),
                         image: UploadFile = File(...),
                         db: Session = Depends(get_db)):
    try:
        db_product = ProductDB(**product.dict())
        db.add(db_product)
        db.commit()

        if image:
            fileName = save_upload_file(image, db_product.id)
            product_db = db.query(ProductDB).filter(
                ProductDB.id == db_product.id)
            product_db.update({ProductDB.image: fileName})
            db.commit()

        return db_product.as_dict()
    except Exception as e:
        return {"product": "nok", "error": str(e)}


@router.get("/{id}")
def get_product_by_id(id: str):
    return {"id": id}
