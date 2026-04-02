from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.wishlist import AddToWishlistRequest, WishlistResponse
from app.services.wishlist_service import (
    add_to_wishlist,
    get_user_wishlist,
    remove_from_wishlist,
    is_in_wishlist
)

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


@router.post("/add", response_model=WishlistResponse)
def add_wishlist_item(request: AddToWishlistRequest, db: Session = Depends(get_db)):
    return add_to_wishlist(db, request.user_id, request.product_id)


@router.get("/user/{user_id}", response_model=list[WishlistResponse])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    return get_user_wishlist(db, user_id)


@router.delete("/remove")
def delete_wishlist_item(user_id: int, product_id: int, db: Session = Depends(get_db)):
    return remove_from_wishlist(db, user_id, product_id)


@router.get("/check")
def check_wishlist(user_id: int, product_id: int, db: Session = Depends(get_db)):
    return is_in_wishlist(db, user_id, product_id)