from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.cart import AddToCartRequest, UpdateCartRequest, MergeGuestCartRequest
from app.services.cart_service import (
    add_to_cart_service,
    get_user_cart_service,
    get_guest_cart_service,
    update_cart_service,
    delete_cart_item_service,
    merge_guest_cart_service,
)

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/add")
def add_item(data: AddToCartRequest, db: Session = Depends(get_db)):
    return add_to_cart_service(
        db=db,
        variant_id=data.variant_id,
        quantity=data.quantity,
        user_id=data.user_id,
        guest_id=data.guest_id,
    )


@router.get("/user/{user_id}")
def get_user_cart(user_id: int, db: Session = Depends(get_db)):
    return get_user_cart_service(db=db, user_id=user_id)


@router.get("/guest/{guest_id}")
def get_guest_cart(guest_id: str, db: Session = Depends(get_db)):
    return get_guest_cart_service(db=db, guest_id=guest_id)


@router.put("/update")
def update_item(data: UpdateCartRequest, db: Session = Depends(get_db)):
    return update_cart_service(
        db=db,
        cart_item_id=data.cart_item_id,
        quantity=data.quantity
    )


@router.delete("/delete/{cart_item_id}")
def delete_item(cart_item_id: int, db: Session = Depends(get_db)):
    return delete_cart_item_service(db=db, cart_item_id=cart_item_id)


@router.post("/merge")
def merge_cart(data: MergeGuestCartRequest, db: Session = Depends(get_db)):
    return merge_guest_cart_service(
        db=db,
        guest_id=data.guest_id,
        user_id=data.user_id
    )