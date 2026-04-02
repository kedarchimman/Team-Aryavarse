from sqlalchemy.orm import Session
from app.repositories.cart_repo import (
    add_to_cart,
    get_cart_by_user,
    get_cart_by_guest,
    update_cart,
    delete_cart_item,
    merge_guest_cart_to_user
)


def add_to_cart_service(
    db: Session,
    variant_id: int,
    quantity: int,
    user_id: int = None,
    guest_id: str = None
):
    return add_to_cart(
        db=db,
        variant_id=variant_id,
        quantity=quantity,
        user_id=user_id,
        guest_id=guest_id
    )


def get_user_cart_service(db: Session, user_id: int):
    return get_cart_by_user(db=db, user_id=user_id)


def get_guest_cart_service(db: Session, guest_id: str):
    return get_cart_by_guest(db=db, guest_id=guest_id)


def update_cart_service(db: Session, cart_item_id: int, quantity: int):
    return update_cart(
        db=db,
        cart_item_id=cart_item_id,
        quantity=quantity
    )


def delete_cart_item_service(db: Session, cart_item_id: int):
    return delete_cart_item(
        db=db,
        cart_item_id=cart_item_id
    )


def merge_guest_cart_service(db: Session, guest_id: str, user_id: int):
    return merge_guest_cart_to_user(
        db=db,
        guest_id=guest_id,
        user_id=user_id
    )