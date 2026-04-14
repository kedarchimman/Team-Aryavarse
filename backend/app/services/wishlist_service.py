from sqlalchemy.orm import Session
from sqlalchemy import text

def get_or_create_wishlist(db: Session, user_id=None, guest_uuid=None):
    if user_id:
        result = db.execute(text("SELECT id FROM wishlist WHERE user_id = :uid"), {"uid": user_id}).fetchone()
        if result:
            return result[0]
        result = db.execute(text("INSERT INTO wishlist (user_id) VALUES (:uid) RETURNING id"), {"uid": user_id}).fetchone()
        db.commit()
        return result[0]
    if guest_uuid:
        result = db.execute(text("SELECT id FROM wishlist WHERE guest_uuid = :g"), {"g": guest_uuid}).fetchone()
        if result:
            return result[0]
        result = db.execute(text("INSERT INTO wishlist (guest_uuid) VALUES (:g) RETURNING id"), {"g": guest_uuid}).fetchone()
        db.commit()
        return result[0]
    return None

def add_to_wishlist(db: Session, wishlist_id: int, variant_id: int):
    db.execute(text("CALL sp_add_to_wishlist(:wid, :vid)"), {"wid": wishlist_id, "vid": variant_id})
    db.commit()

def remove_from_wishlist(db: Session, wishlist_id: int, variant_id: int):
    db.execute(text("CALL sp_remove_from_wishlist(:wid, :vid)"), {"wid": wishlist_id, "vid": variant_id})
    db.commit()

def merge_wishlist(db: Session, guest_uuid: str, user_id: int):
    db.execute(text("CALL sp_merge_wishlist(:g, :u)"), {"g": guest_uuid, "u": user_id})
    db.commit()

def get_wishlist(db: Session, user_id=None, guest_uuid=None):
    if user_id:
        result = db.execute(text("SELECT * FROM wishlist_view WHERE user_id = :uid"), {"uid": user_id})
    elif guest_uuid:
        result = db.execute(text("SELECT * FROM wishlist_view WHERE guest_uuid = :g"), {"g": guest_uuid})
    else:
        return []
    rows = result.fetchall()
    return [dict(row._mapping) for row in rows]