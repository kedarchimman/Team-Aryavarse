from sqlalchemy import Column, Integer,String, Text, ForeignKey, Float
from app.db.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variant"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    variant_name = Column(Text)
    color = Column(String) 
    price = Column(Float)
    stock = Column(Integer)
    sku = Column(Text)