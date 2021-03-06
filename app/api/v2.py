from fastapi import APIRouter, Depends
from app.api import authen, product, transaction
from app.models import database
from app.api import security
database.Base.metadata.create_all(database.engine, checkfirst=True)

api_router = APIRouter()


api_router.include_router(authen.router,
                          tags=["authen"])

api_router.include_router(product.router,
                          prefix="/product",
                          tags=["product"],
                          dependencies=[Depends(security.checkAuthorized)])

api_router.include_router(transaction.router,
                          prefix="/transaction",
                          tags=["transaction"],
                          dependencies=[Depends(security.checkAuthorized)])
