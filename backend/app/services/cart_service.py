from sqlalchemy.orm import Session
from app.models.cart import CartItem


#  ADD TO CART
def add_to_cart(db: Session, product_id: int, quantity: int, user_id=None, guest_id=None):

    
    if user_id == 0:
        user_id = None
    if guest_id == 0:
        guest_id = None

    if quantity <= 0:
        return {"error": "Quantity must be greater than 0"}

    if user_id is None and guest_id is None:
        return {"error": "user_id or guest_id required"}

    #  
    query = db.query(CartItem).filter(CartItem.product_id == product_id)

    if user_id is not None:
        query = query.filter(CartItem.user_id == user_id)
    else:
        query = query.filter(CartItem.guest_id == guest_id)

    existing_item = query.first()

    if existing_item:
        existing_item.quantity += quantity
        db.commit()
        db.refresh(existing_item)
        return existing_item

    new_item = CartItem(
        product_id=product_id,
        quantity=quantity,
        user_id=user_id,
        guest_id=guest_id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


#  GET USER CART
def get_cart_by_user(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()


#  GET GUEST CART
def get_cart_by_guest(db: Session, guest_id: str):
    return db.query(CartItem).filter(CartItem.guest_id == guest_id).all()


#  UPDATE CART
def update_cart(db: Session, cart_item_id: int, quantity: int):
    item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()

    if not item:
        return {"error": "Item not found"}

    if quantity <= 0:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted"}

    item.quantity = quantity
    db.commit()
    db.refresh(item)
    return item


#  DELETE CART ITEM
def delete_cart_item(db: Session, cart_item_id: int):
    item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()

    if not item:
        return {"error": "Item not found"}

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}


#  MERGE GUEST → USER CART
def merge_guest_cart_to_user(db: Session, guest_id: str, user_id: int):

    if not guest_id or not user_id:
        return {"error": "guest_id and user_id required"}

    guest_items = db.query(CartItem).filter(CartItem.guest_id == guest_id).all()

    for guest_item in guest_items:
        existing_user_item = db.query(CartItem).filter(
            CartItem.user_id == user_id,
            CartItem.product_id == guest_item.product_id
        ).first()

        if existing_user_item:
            existing_user_item.quantity += guest_item.quantity
            db.delete(guest_item)
        else:
            guest_item.user_id = user_id
            guest_item.guest_id = None

    db.commit()

    return {"message": "Cart merged successfully"}