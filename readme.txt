source : https://github.com/codemobiles/cm_fastapi_cmstock_workshop

- pip3 install pipenv
- pipenv shell
- pipenv install fastapi sqlalchemy pydantic
- uvicorn app.main:app --reload --port 8081