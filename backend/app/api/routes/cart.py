from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.cart import AddToCartRequest, UpdateCartRequest, MergeGuestCartRequest
from app.services.cart_service import (
    add_to_cart,
    get_cart_by_user,
    get_cart_by_guest,
    update_cart,
    delete_cart_item,
    merge_guest_cart_to_user,
)

router = APIRouter(prefix="/cart", tags=["Cart"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
def add_item(data: AddToCartRequest, db: Session = Depends(get_db)):
    return add_to_cart(
        db=db,
        product_id=data.product_id,
        quantity=data.quantity,
        user_id=data.user_id,
        guest_id=data.guest_id,
    )


@router.get("/user/{user_id}")
def get_user_cart(user_id: int, db: Session = Depends(get_db)):
    return get_cart_by_user(db, user_id)


@router.get("/guest/{guest_id}")
def get_guest_cart(guest_id: str, db: Session = Depends(get_db)):
    return get_cart_by_guest(db, guest_id)


@router.put("/update")
def update_item(data: UpdateCartRequest, db: Session = Depends(get_db)):
    return update_cart(db, data.cart_item_id, data.quantity)


@router.delete("/delete/{cart_item_id}")
def delete_item(cart_item_id: int, db: Session = Depends(get_db)):
    return delete_cart_item(db, cart_item_id)


@router.post("/merge")
def merge_cart(data: MergeGuestCartRequest, db: Session = Depends(get_db)):
    return merge_guest_cart_to_user(db, data.guest_id, data.user_id)