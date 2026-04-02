from sqlalchemy.orm import Session
from sqlalchemy import text


def get_or_create_cart(db: Session, user_id: int = None, guest_id: str = None):
    try:
        if user_id is None and guest_id is None:
            return None

        if user_id is not None:
            result = db.execute(
                text("SELECT id FROM cart WHERE user_id = :user_id LIMIT 1"),
                {"user_id": user_id}
            )
            row = result.fetchone()

            if row:
                return row[0]

            db.execute(
                text("""
                    INSERT INTO cart (user_id, guest_id)
                    VALUES (:user_id, NULL)
                """),
                {"user_id": user_id}
            )
            db.commit()

            result = db.execute(
                text("SELECT id FROM cart WHERE user_id = :user_id ORDER BY id DESC LIMIT 1"),
                {"user_id": user_id}
            )
            row = result.fetchone()
            return row[0] if row else None

        result = db.execute(
            text("SELECT id FROM cart WHERE guest_id = :guest_id LIMIT 1"),
            {"guest_id": guest_id}
        )
        row = result.fetchone()

        if row:
            return row[0]

        db.execute(
            text("""
                INSERT INTO cart (user_id, guest_id)
                VALUES (NULL, :guest_id)
            """),
            {"guest_id": guest_id}
        )
        db.commit()

        result = db.execute(
            text("SELECT id FROM cart WHERE guest_id = :guest_id ORDER BY id DESC LIMIT 1"),
            {"guest_id": guest_id}
        )
        row = result.fetchone()
        return row[0] if row else None

    except Exception:
        db.rollback()
        return None


def add_to_cart(db: Session, variant_id: int, quantity: int, user_id: int = None, guest_id: str = None):
    try:
        if user_id == 0:
            user_id = None

        if quantity <= 0:
            return {"error": "Quantity must be greater than 0"}

        if user_id is None and guest_id is None:
            return {"error": "user_id or guest_id required"}

        cart_id = get_or_create_cart(db, user_id=user_id, guest_id=guest_id)

        if cart_id is None:
            return {"error": "Cart not found or created"}

        db.execute(
            text("""
                CALL sp_add_to_cart(
                    :cart_id,
                    :variant_id,
                    :quantity
                )
            """),
            {
                "cart_id": cart_id,
                "variant_id": variant_id,
                "quantity": quantity
            }
        )
        db.commit()

        result = db.execute(
            text("""
                SELECT *
                FROM cart_item
                WHERE cart_id = :cart_id
                  AND variant_id = :variant_id
                LIMIT 1
            """),
            {
                "cart_id": cart_id,
                "variant_id": variant_id
            }
        )
        row = result.fetchone()

        if row:
            return dict(row._mapping)

        return {
            "message": "Item added to cart successfully",
            "cart_id": cart_id,
            "variant_id": variant_id,
            "quantity": quantity
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}


def get_cart_by_user(db: Session, user_id: int):
    try:
        result = db.execute(
            text("""
                SELECT ci.*
                FROM cart_item ci
                JOIN cart c ON c.id = ci.cart_id
                WHERE c.user_id = :user_id
            """),
            {"user_id": user_id}
        )
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    except Exception as e:
        return {"error": str(e)}


def get_cart_by_guest(db: Session, guest_id: str):
    try:
        result = db.execute(
            text("""
                SELECT ci.*
                FROM cart_item ci
                JOIN cart c ON c.id = ci.cart_id
                WHERE c.guest_id = :guest_id
            """),
            {"guest_id": guest_id}
        )
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    except Exception as e:
        return {"error": str(e)}


def update_cart(db: Session, cart_item_id: int, quantity: int):
    try:
        db.execute(
            text("CALL sp_update_cart_item(:cart_item_id, :quantity)"),
            {
                "cart_item_id": cart_item_id,
                "quantity": quantity
            }
        )
        db.commit()

        if quantity <= 0:
            return {"message": "Item deleted"}

        result = db.execute(
            text("SELECT * FROM cart_item WHERE id = :cart_item_id"),
            {"cart_item_id": cart_item_id}
        )
        row = result.fetchone()

        if not row:
            return {"error": "Item not found"}

        return dict(row._mapping)

    except Exception as e:
        db.rollback()
        return {"error": str(e)}


def delete_cart_item(db: Session, cart_item_id: int):
    try:
        db.execute(
            text("CALL sp_delete_cart_item(:cart_item_id)"),
            {"cart_item_id": cart_item_id}
        )
        db.commit()
        return {"message": "Item deleted"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}


def merge_guest_cart_to_user(db: Session, guest_id: str, user_id: int):
    try:
        if guest_id is None or user_id is None:
            return {"error": "guest_id and user_id required"}

        db.execute(
            text("""
                CALL sp_merge_guest_cart_to_user(
                    CAST(:guest_id AS VARCHAR),
                    CAST(:user_id AS INTEGER)
                )
            """),
            {
                "guest_uuid": guest_uuid,
                "user_id": user_id
            }
        )
        db.commit()

        return {"message": "Cart merged successfully"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}