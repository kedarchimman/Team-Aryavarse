from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

from app.models.cart import CartItem
from app.models.user import User
from app.models.guest import GuestSession

DATABASE_URL = "postgresql://postgres:akash45@localhost:5432/ecommerce"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)