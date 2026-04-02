from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from app.db.session import Base


class Product(Base):
    __tablename__ = "product"   #  FIXED

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    is_recommended = Column(Boolean, default=False)

    #  relation with category table
    category_id = Column(Integer, ForeignKey("category.id"), nullable=True)