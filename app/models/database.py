from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./cmstock.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/cmfaststock?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
