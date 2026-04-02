from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

from app.models.cart import CartItem
from app.models.user import User
from app.models.guest import GuestSession
from app.models.product import Product
from app.models.wishlist import WishlistItem

DATABASE_URL = "postgresql://postgres:akash45@localhost:5432/ecommerce"

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()