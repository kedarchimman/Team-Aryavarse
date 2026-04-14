from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from app.core.database import get_db
from app.schemas.cart import AddToCart
from app.services import cart_service

router = APIRouter(prefix="/cart", tags=["Cart"])

class UpdateQty(BaseModel):
    quantity: int

@router.post("/guest")
def create_guest(db: Session = Depends(get_db)):
    guest_uuid = cart_service.get_or_create_guest(db)
    return {"message": "Guest created", "guest_uuid": guest_uuid}

@router.get("/")
def get_cart(db: Session = Depends(get_db),
             user_id: Optional[int] = None,
             guest_uuid: Optional[str] = Header(None, alias="guest-uuid")):
    if not user_id and not guest_uuid:
        raise HTTPException(400, "Provide user_id or guest_uuid")
    cart = cart_service.get_cart(db, user_id, guest_uuid)
    return {"count": len(cart), "items": cart}

@router.post("/add")
def add_item(data: AddToCart, db: Session = Depends(get_db),
             user_id: Optional[int] = None,
             guest_uuid: Optional[str] = Header(None, alias="guest-uuid")):
    if not user_id and not guest_uuid:
        raise HTTPException(400, "Provide user_id or guest_uuid")
    cart_id = cart_service.get_or_create_cart(db, user_id, guest_uuid)
    cart_service.add_to_cart(db, cart_id, data.variant_id, data.quantity)
    return {"message": "Item added", "cart_id": cart_id}

@router.delete("/remove/{cart_item_id}")
def remove_item(cart_item_id: int, db: Session = Depends(get_db),
                user_id: Optional[int] = None,
                guest_uuid: Optional[str] = Header(None, alias="guest-uuid")):
    if not user_id and not guest_uuid:
        raise HTTPException(400, "Provide user_id or guest_uuid")
    cart_service.remove_from_cart(db, cart_item_id)
    return {"message": "Item removed"}

@router.patch("/update/{cart_item_id}")
def update_qty(cart_item_id: int, data: UpdateQty, db: Session = Depends(get_db),
               user_id: Optional[int] = None,
               guest_uuid: Optional[str] = Header(None, alias="guest-uuid")):
    if not user_id and not guest_uuid:
        raise HTTPException(400, "Provide user_id or guest_uuid")
    if data.quantity <= 0:
        raise HTTPException(400, "Quantity must be > 0")
    cart_service.update_cart_qty(db, cart_item_id, data.quantity)
    return {"message": "Quantity updated"}

@router.post("/merge")
def merge_cart(user_id: int, guest_uuid: str, db: Session = Depends(get_db)):
    cart_service.merge_cart(db, guest_uuid, user_id)
    return {"message": "Cart merged"}