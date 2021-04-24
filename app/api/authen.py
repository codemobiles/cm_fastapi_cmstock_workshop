from fastapi import APIRouter

router = APIRouter()


@router.get("/authen")
def get_authen():
    return {"result": "authen"}
