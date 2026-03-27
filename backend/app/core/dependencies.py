from sqlalchemy.orm import Session
from fastapi import Depends, Header, HTTPException, status

from app.db.session import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user_optional(x_user_id: str = Header(default=None)):
    if x_user_id:
        return {"id": int(x_user_id)}
    return None


def get_current_user_required(current_user=Depends(get_current_user_optional)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login required"
        )
    return current_user