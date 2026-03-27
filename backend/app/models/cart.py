from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    
    guest_id = Column(String, nullable=True)