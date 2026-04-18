from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.cart_service import (
    get_or_create_guest,
    get_or_create_cart,
    add_to_cart as add_to_cart_service,
    get_cart as get_cart_service,
    update_cart_qty,
    remove_from_cart,
    merge_guest_cart,
)

router = APIRouter(prefix="/cart", tags=["Cart"])


class AddToCartRequest(BaseModel):
    variant_id: int
    quantity: int
    user_id: int | None = None
    guest_uuid: str | None = None


class UpdateCartRequest(BaseModel):
    cart_item_id: int
    quantity: int
    user_id: int | None = None
    guest_uuid: str | None = None


class RemoveCartRequest(BaseModel):
    cart_item_id: int
    user_id: int | None = None
    guest_uuid: str | None = None


class MergeCartRequest(BaseModel):
    guest_uuid: str
    user_id: int


@router.post("/guest")
def create_guest(db: Session = Depends(get_db)):
    guest_uuid = get_or_create_guest(db)
    return {"guest_uuid": guest_uuid}


@router.get("/")
def get_cart(
    user_id: int | None = None,
    guest_uuid: str | None = None,
    db: Session = Depends(get_db)
):
    if user_id is None and guest_uuid is None:
        raise HTTPException(status_code=400, detail="user_id or guest_uuid is required")

    items = get_cart_service(db, user_id=user_id, guest_uuid=guest_uuid)
    return {"items": items}


@router.post("/add")
def add_to_cart(data: AddToCartRequest, db: Session = Depends(get_db)):
    if data.user_id is None and data.guest_uuid is None:
        raise HTTPException(status_code=400, detail="user_id or guest_uuid is required")

    if data.quantity <= 0:
        raise HTTPException(status_code=400, detail="quantity must be greater than 0")

    try:
        cart_id = get_or_create_cart(
            db,
            user_id=data.user_id,
            guest_uuid=data.guest_uuid
        )

        if not cart_id:
            raise HTTPException(status_code=500, detail="Could not get or create cart")

        add_to_cart_service(db, cart_id, data.variant_id, data.quantity)
        return {"message": "Added to cart successfully"}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Cart error: {str(e)}")


@router.put("/update")
def update_cart(data: UpdateCartRequest, db: Session = Depends(get_db)):
    if data.quantity <= 0:
        raise HTTPException(status_code=400, detail="quantity must be greater than 0")
    try:
        update_cart_qty(db, data.cart_item_id, data.quantity)
        return {"message": "Cart updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Update error: {str(e)}")


@router.delete("/remove")
def remove_cart_item(data: RemoveCartRequest = Body(...), db: Session = Depends(get_db)):
    try:
        remove_from_cart(db, data.cart_item_id)
        return {"message": "Item removed successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Remove error: {str(e)}")


@router.post("/merge")
def merge_cart(data: MergeCartRequest, db: Session = Depends(get_db)):
    try:
        merge_guest_cart(db, data.guest_uuid, data.user_id)
        return {"message": "Cart merged successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Merge error: {str(e)}")