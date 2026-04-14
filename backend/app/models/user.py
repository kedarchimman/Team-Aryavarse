from sqlalchemy import Column, Integer, String, Boolean, Text
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text)
    user_type = Column(Text)
    keycloak_id = Column(Text)
    is_email_verified = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)