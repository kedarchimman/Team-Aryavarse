from typing import Optional, Dict, Any, List
from sqlalchemy import text
from sqlalchemy.orm import Session


def get_cart_id_by_user_id(db: Session, user_id: int) -> Optional[int]:
    query = text("""
        SELECT id
        FROM cart
        WHERE user_id = :user_id
        ORDER BY id DESC
        LIMIT 1
    """)
    result = db.execute(query, {"user_id": user_id}).scalar()
    return result


def is_valid_user_address(db: Session, user_id: int, address_id: int) -> bool:
    query = text("""
        SELECT 1
        FROM address
        WHERE id = :address_id
          AND user_id = :user_id
        LIMIT 1
    """)
    result = db.execute(
        query,
        {"address_id": address_id, "user_id": user_id}
    ).scalar()
    return result is not None


def get_order_by_id(db: Session, order_id: int) -> Optional[Dict[str, Any]]:
    query = text("""
        SELECT
            id,
            user_id,
            address_id,
            total_amount,
            status,
            payment_status,
            created_at,
            updated_at
        FROM orders
        WHERE id = :order_id
    """)
    row = db.execute(query, {"order_id": order_id}).mappings().first()
    return dict(row) if row else None


def get_order_items_by_order_id(db: Session, order_id: int) -> List[Dict[str, Any]]:
    query = text("""
        SELECT
            oi.id,
            oi.order_id,
            oi.variant_id,
            oi.quantity,
            oi.price,
            oi.created_at
        FROM order_items oi
        WHERE oi.order_id = :order_id
        ORDER BY oi.id
    """)
    rows = db.execute(query, {"order_id": order_id}).mappings().all()
    return [dict(row) for row in rows]


def call_sp_process_payment(
    db: Session,
    order_id: int,
    payment_method: str,
    payment_status: str,
    transaction_ref: str
) -> None:
    db.execute(
        text("""
            CALL sp_process_payment(
                :order_id,
                :payment_method,
                :payment_status,
                :transaction_ref
            )
        """),
        {
            "order_id": order_id,
            "payment_method": payment_method,
            "payment_status": payment_status,
            "transaction_ref": transaction_ref
        }
    )


def transaction_ref_exists(db: Session, transaction_ref: str) -> bool:
    query = text("""
        SELECT 1
        FROM transactions
        WHERE transaction_ref = :transaction_ref
        LIMIT 1
    """)
    result = db.execute(query, {"transaction_ref": transaction_ref}).scalar()
    return result is not None