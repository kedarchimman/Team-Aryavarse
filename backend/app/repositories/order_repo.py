from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.shipment import Shipment
from app.models.order_status_history import OrderStatusHistory
from app.models.return_request import ReturnRequest
from typing import Optional


class OrderRepository:

    # ─── Get Orders (Admin) ───────────────────────────────────────────────────
    @staticmethod
    def get_all_orders(db: Session, status: Optional[str] = None, payment_status: Optional[str] = None):
        query = db.query(Order)
        if status:
            query = query.filter(Order.status == status.upper())
        if payment_status:
            query = query.filter(Order.payment_status == payment_status.upper())
        return query.order_by(Order.created_at.desc()).all()

    @staticmethod
    def get_order_by_id(db: Session, order_id: int):
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_orders_by_user(db: Session, user_id: int):
        return db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()

    # ─── Update Order Status (uses SP) ───────────────────────────────────────
    @staticmethod
    def update_order_status(db: Session, order_id: int, new_status: str):
        db.execute(
            text("CALL sp_update_order_status(:oid, :status)"),
            {"oid": order_id, "status": new_status.upper()}
        )
        db.commit()
        return db.query(Order).filter(Order.id == order_id).first()

    # ─── Cancel Order (uses SP) ───────────────────────────────────────────────
    @staticmethod
    def cancel_order(db: Session, order_id: int):
        db.execute(
            text("CALL sp_cancel_order(:oid)"),
            {"oid": order_id}
        )
        db.commit()
        return db.query(Order).filter(Order.id == order_id).first()

    # ─── Order Items ──────────────────────────────────────────────────────────
    @staticmethod
    def get_order_items(db: Session, order_id: int):
        return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()

    # ─── Order Status History ─────────────────────────────────────────────────
    @staticmethod
    def get_order_status_history(db: Session, order_id: int):
        return db.query(OrderStatusHistory).filter(
            OrderStatusHistory.order_id == order_id
        ).order_by(OrderStatusHistory.changed_at.asc()).all()

    # ─── Shipment ─────────────────────────────────────────────────────────────
    @staticmethod
    def create_shipment(db: Session, order_id: int, data):
        db.execute(
            text("CALL sp_create_shipment(:oid, :courier, :tracking, :est_delivery)"),
            {
                "oid": order_id,
                "courier": data.courier_name,
                "tracking": data.tracking_number,
                "est_delivery": data.estimated_delivery,
            }
        )
        db.commit()
        return db.query(Shipment).filter(Shipment.order_id == order_id).first()

    @staticmethod
    def update_shipment_status(db: Session, tracking_number: str, status: str):
        db.execute(
            text("CALL sp_update_shipment_status(:tracking, :status)"),
            {"tracking": tracking_number, "status": status.upper()}
        )
        db.commit()
        return db.query(Shipment).filter(Shipment.tracking_number == tracking_number).first()

    @staticmethod
    def get_shipment_by_order(db: Session, order_id: int):
        return db.query(Shipment).filter(Shipment.order_id == order_id).first()

    # ─── Return Requests ──────────────────────────────────────────────────────
    @staticmethod
    def create_return_request(db: Session, user_id: int, data):
        db.execute(
            text("CALL sp_create_return_request(:order_id, :item_id, :user_id, :qty, :reason)"),
            {
                "order_id": data.order_id,
                "item_id": data.order_item_id,
                "user_id": user_id,
                "qty": data.quantity,
                "reason": data.reason,
            }
        )
        db.commit()
        return db.query(ReturnRequest).filter(
            ReturnRequest.order_id == data.order_id,
            ReturnRequest.user_id == user_id,
        ).order_by(ReturnRequest.created_at.desc()).first()

    @staticmethod
    def get_all_return_requests(db: Session, status: Optional[str] = None):
        query = db.query(ReturnRequest)
        if status:
            query = query.filter(ReturnRequest.status == status.upper())
        return query.order_by(ReturnRequest.created_at.desc()).all()

    @staticmethod
    def get_return_request_by_id(db: Session, return_id: int):
        return db.query(ReturnRequest).filter(ReturnRequest.id == return_id).first()

    @staticmethod
    def approve_return_request(db: Session, return_id: int, refund_method: str):
        db.execute(
            text("CALL sp_approve_return_request(:rid, :method)"),
            {"rid": return_id, "method": refund_method.upper()}
        )
        db.commit()
        return db.query(ReturnRequest).filter(ReturnRequest.id == return_id).first()

    @staticmethod
    def complete_refund(db: Session, return_id: int):
        db.execute(
            text("CALL sp_complete_refund(:rid)"),
            {"rid": return_id}
        )
        db.commit()
        return db.query(ReturnRequest).filter(ReturnRequest.id == return_id).first()

    # ─── Analytics View ───────────────────────────────────────────────────────
    @staticmethod
    def get_order_view(db: Session, order_id: Optional[int] = None):
        if order_id:
            result = db.execute(
                text("SELECT * FROM order_view WHERE order_id = :oid"),
                {"oid": order_id}
            )
        else:
            result = db.execute(text("SELECT * FROM order_view LIMIT 100"))
        return result.mappings().all()

    @staticmethod
    def get_top_selling_products(db: Session):
        result = db.execute(text("SELECT * FROM top_selling_products LIMIT 20"))
        return result.mappings().all()

    @staticmethod
    def get_return_requests_view(db: Session):
        result = db.execute(text("SELECT * FROM return_request_view"))
        return result.mappings().all()