from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_admin

router = APIRouter(prefix="/admin/inventory", tags=["Admin Inventory"])


@router.get("/")
def get_inventory(
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    return {"message": "Inventory working"}