
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variant"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    color = Column(String, nullable=True)
    size = Column(String, nullable=True)