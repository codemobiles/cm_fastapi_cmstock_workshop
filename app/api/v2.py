from fastapi import APIRouter
from app.api import authen, product, transaction

api_router = APIRouter()


api_router.include_router(authen.router,
                          tags=["authen"])

api_router.include_router(product.router,
                          prefix="/product",
                          tags=["product"])

api_router.include_router(transaction.router,
                          prefix="/transaction",
                          tags=["transaction"])
