from fastapi import FastAPI
from app.api.v2 import api_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/images", StaticFiles(directory="uploaded/images",
          html=True), name="images")

# app.include_router(api_router, prefix="/api/v1")
app.include_router(api_router, prefix="/api/v2")