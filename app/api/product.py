from fastapi import APIRouter

router = APIRouter()

@router.get("/product")
def get_product():
    return {"result": "product"}