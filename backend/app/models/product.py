from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.db.base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    sku = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    is_deleted = Column(Boolean, default=False)