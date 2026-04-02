from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.wishlist import WishlistItem
from app.models.product import Product
from app.models.user import User


def add_to_wishlist(db: Session, user_id: int, product_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing = db.query(WishlistItem).filter(
        WishlistItem.user_id == user_id,
        WishlistItem.product_id == product_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Product already in wishlist")

    wishlist_item = WishlistItem(user_id=user_id, product_id=product_id)
    db.add(wishlist_item)
    db.commit()
    db.refresh(wishlist_item)
    return wishlist_item


def get_user_wishlist(db: Session, user_id: int):
    return db.query(WishlistItem).filter(WishlistItem.user_id == user_id).all()


def remove_from_wishlist(db: Session, user_id: int, product_id: int):
    wishlist_item = db.query(WishlistItem).filter(
        WishlistItem.user_id == user_id,
        WishlistItem.product_id == product_id
    ).first()

    if not wishlist_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found")

    db.delete(wishlist_item)
    db.commit()
    return {"message": "Product removed from wishlist"}


def is_in_wishlist(db: Session, user_id: int, product_id: int):
    wishlist_item = db.query(WishlistItem).filter(
        WishlistItem.user_id == user_id,
        WishlistItem.product_id == product_id
    ).first()

    return {"in_wishlist": wishlist_item is not None}