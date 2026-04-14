import uuid
from sqlalchemy.orm import Session
from sqlalchemy import text


def get_or_create_guest(db: Session) -> str:
    """Creates a new guest UUID in the guest table and returns it."""
    new_uuid = str(uuid.uuid4())
    db.execute(
        text("INSERT INTO guest (uuid) VALUES (:uuid) ON CONFLICT (uuid) DO NOTHING"),
        {"uuid": new_uuid}
    )
    db.commit()
    return new_uuid


def get_or_create_cart(db: Session, user_id: int = None, guest_uuid: str = None) -> int:
    """Gets existing cart or creates one. Returns cart id."""

    if user_id:
        row = db.execute(
            text("SELECT id FROM cart WHERE user_id = :uid"),
            {"uid": user_id}
        ).fetchone()
        if row:
            return row[0]

        row = db.execute(
            text("INSERT INTO cart (user_id) VALUES (:uid) RETURNING id"),
            {"uid": user_id}
        ).fetchone()
        db.commit()
        return row[0]

    elif guest_uuid:
        # Step 1: Ensure guest row exists — cart.guest_uuid has FK → guest.uuid
        db.execute(
            text("INSERT INTO guest (uuid) VALUES (:uuid) ON CONFLICT (uuid) DO NOTHING"),
            {"uuid": guest_uuid}
        )
        db.commit()

        # Step 2: Get or create cart for this guest
        row = db.execute(
            text("SELECT id FROM cart WHERE guest_uuid = :guuid"),
            {"guuid": guest_uuid}
        ).fetchone()
        if row:
            return row[0]

        row = db.execute(
            text("INSERT INTO cart (guest_uuid) VALUES (:guuid) RETURNING id"),
            {"guuid": guest_uuid}
        ).fetchone()
        db.commit()
        return row[0]

    return None


def add_to_cart(db: Session, cart_id: int, variant_id: int, quantity: int):
    """Add item to cart. If already exists, increment quantity."""
    db.execute(
        text("""
            INSERT INTO cart_item (cart_id, variant_id, quantity)
            VALUES (:cart_id, :variant_id, :quantity)
            ON CONFLICT (cart_id, variant_id)
            DO UPDATE SET quantity = cart_item.quantity + EXCLUDED.quantity
        """),
        {"cart_id": cart_id, "variant_id": variant_id, "quantity": quantity}
    )
    db.commit()


def get_cart(db: Session, user_id: int = None, guest_uuid: str = None) -> list:
    """Returns all cart items with product details."""
    if user_id:
        condition = "c.user_id = :identifier"
        identifier = user_id
    elif guest_uuid:
        condition = "c.guest_uuid = :identifier"
        identifier = guest_uuid
    else:
        return []

    rows = db.execute(
        text(f"""
            SELECT
                ci.id            AS id,
                ci.variant_id    AS variant_id,
                ci.quantity      AS quantity,
                pv.price         AS price,
                pv.variant_name  AS variant_name,
                p.name           AS product_name,
                pi.image_url     AS image_url
            FROM cart c
            JOIN cart_item ci       ON ci.cart_id = c.id
            JOIN product_variant pv ON pv.id = ci.variant_id
            JOIN product p          ON p.id = pv.product_id
            LEFT JOIN product_image pi
                ON pi.product_id = p.id AND pi.is_primary = TRUE
            WHERE {condition}
        """),
        {"identifier": identifier}
    ).fetchall()

    return [
        {
            "id":           row[0],
            "variant_id":   row[1],
            "quantity":     row[2],
            "price":        float(row[3]),
            "variant_name": row[4] or "",
            "product_name": row[5] or "Product",
            "image_url":    row[6] or "",
        }
        for row in rows
    ]


def update_cart_qty(db: Session, cart_item_id: int, quantity: int):
    db.execute(
        text("UPDATE cart_item SET quantity = :qty WHERE id = :id"),
        {"qty": quantity, "id": cart_item_id}
    )
    db.commit()


def remove_from_cart(db: Session, cart_item_id: int):
    db.execute(
        text("DELETE FROM cart_item WHERE id = :id"),
        {"id": cart_item_id}
    )
    db.commit()


def merge_guest_cart(db: Session, guest_uuid: str, user_id: int):
    """Merges guest cart into user cart on login."""
    guest_cart = db.execute(
        text("SELECT id FROM cart WHERE guest_uuid = :guuid"),
        {"guuid": guest_uuid}
    ).fetchone()

    if not guest_cart:
        return  # Nothing to merge

    guest_cart_id = guest_cart[0]

    # Get or create user cart
    user_cart = db.execute(
        text("SELECT id FROM cart WHERE user_id = :uid"),
        {"uid": user_id}
    ).fetchone()

    if not user_cart:
        user_cart = db.execute(
            text("INSERT INTO cart (user_id) VALUES (:uid) RETURNING id"),
            {"uid": user_id}
        ).fetchone()
        db.commit()

    user_cart_id = user_cart[0]

    # Merge: add guest items into user cart, increment if already exists
    db.execute(
        text("""
            INSERT INTO cart_item (cart_id, variant_id, quantity)
            SELECT :user_cart_id, variant_id, quantity
            FROM cart_item
            WHERE cart_id = :guest_cart_id
            ON CONFLICT (cart_id, variant_id)
            DO UPDATE SET quantity = cart_item.quantity + EXCLUDED.quantity
        """),
        {"user_cart_id": user_cart_id, "guest_cart_id": guest_cart_id}
    )

    # Clean up guest cart
    db.execute(text("DELETE FROM cart_item WHERE cart_id = :id"), {"id": guest_cart_id})
    db.execute(text("DELETE FROM cart WHERE id = :id"), {"id": guest_cart_id})
    db.commit()