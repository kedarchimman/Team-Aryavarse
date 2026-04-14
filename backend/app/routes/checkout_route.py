from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.checkout import CheckoutRequest, PaymentRequest
from app.services.checkout_service import (
    checkout_service,
    process_payment_service
)

router = APIRouter(prefix="/checkout", tags=["Checkout"])


@router.post("/")
def checkout(data: CheckoutRequest, db: Session = Depends(get_db)):
    return checkout_service(
        db=db,
        user_id=data.user_id,
        address_id=data.address_id,
        coupon_code=data.coupon_code,
        shipping_amount=data.shipping_amount,
        
    )


@router.post("/payment")
def process_payment(data: PaymentRequest, db: Session = Depends(get_db)):
    return process_payment_service(
        db=db,
        order_id=data.order_id,
        payment_method=data.payment_method,
        payment_status=data.payment_status,
        transaction_ref=data.transaction_ref
    )