from sqlalchemy import Column, Integer
from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"   # ⚠️ try this first

    id = Column(Integer, primary_key=True, index=True)