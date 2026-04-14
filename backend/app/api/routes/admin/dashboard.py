from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_admin
from app.services.admin_service import AdminService

router = APIRouter(prefix="/admin", tags=["Admin"])

service = AdminService()


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    return service.get_dashboard_data(db)


@router.get("/users")
def users(
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    return service.get_users(db)


@router.get("/orders")
def orders(
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    return service.get_orders(db)