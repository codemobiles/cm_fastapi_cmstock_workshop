from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_transaction():
    return {"result": "transaction"}
