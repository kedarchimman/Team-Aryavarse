from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_admin

router = APIRouter(prefix="/admin/payments", tags=["Admin Payments"])


@router.get("/")
def get_payments(
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    return {"message": "Payments working"}