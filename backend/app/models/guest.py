from sqlalchemy import Column, Integer, String
from app.db.base import Base


class GuestSession(Base):
    __tablename__ = "guest_sessions"

    guest_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, nullable=True)