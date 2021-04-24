from fastapi import APIRouter

router = APIRouter()

@router.get("/transaction")
def get_transaction():
    return {"result": "transaction"}