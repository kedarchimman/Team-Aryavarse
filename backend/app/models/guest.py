from sqlalchemy import Column, Integer, String
from app.db.base import Base


class GuestSession(Base):
    __tablename__ = "guest"

    guest_id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    session_id = Column(String, unique=True, nullable=True)