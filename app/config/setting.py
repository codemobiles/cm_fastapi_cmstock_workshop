import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):

    # Cors
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:8085"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "CMSTOCK"

    # Security
    SECRET_KEY = "LUHH2xSdq9VF81NI/29whx4cqB2Hug8Aqh6R/uWCnuA="
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30000


class Config:
    case_sensitive = True


settings = Settings()
