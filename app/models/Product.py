import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    stock = Column(Integer)
    price = Column(Float)
    image = Column(String(256))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    class Config:
        arbitrary_types_allowed = True
