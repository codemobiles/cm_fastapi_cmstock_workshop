from fastapi import FastAPI
from app.api.v2 import api_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator



app = FastAPI()
app.mount("/images", StaticFiles(directory="uploaded/images",
          html=True), name="images")


# Set all CORS enabled origins
if True:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:80"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    print("No cors settings")


# app.include_router(api_router, prefix="/api/v1")
app.include_router(api_router, prefix="/api/v2")
