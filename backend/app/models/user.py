from sqlalchemy import Column, Integer, Text, Boolean, String
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.sql import func
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=True)
    phone = Column(Text, nullable=True)
    user_type = Column(Text, nullable=True)        # 'customer' | 'admin'
    guest_id = Column(UUID(as_uuid=True), nullable=True)
    is_deleted = Column(Boolean, default=False)
    keycloak_id = Column(Text, unique=True, nullable=True)
    is_email_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=True)