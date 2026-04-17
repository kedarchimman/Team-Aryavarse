from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    sku = Column(Text, nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    details_and_fit = Column(Text, nullable=True)
    fabric_and_care = Column(Text, nullable=True)
    return_and_exchange = Column(Text, nullable=True)
    tax_rate_id = Column(Integer, ForeignKey("tax_rate.id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    