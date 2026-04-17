from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.order_repo import OrderRepository
from app.schemas.order import (
    OrderStatusUpdate, ShipmentCreate,
    ShipmentStatusUpdate, ReturnRequestCreate, ReturnApprove
)
from typing import Optional


class OrderService:

    # ─── Admin: Get All Orders ────────────────────────────────────────────────
    @staticmethod
    def get_all_orders(db: Session, status: Optional[str] = None, payment_status: Optional[str] = None):
        return OrderRepository.get_all_orders(db, status, payment_status)

    # ─── Get Single Order (with items) ───────────────────────────────────────
    @staticmethod
    def get_order_detail(db: Session, order_id: int):
        order = OrderRepository.get_order_by_id(db, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        items = OrderRepository.get_order_items(db, order_id)
        return order, items

    # ─── Get Orders by User ───────────────────────────────────────────────────
    @staticmethod
    def get_user_orders(db: Session, user_id: int):
        return OrderRepository.get_orders_by_user(db, user_id)

    # ─── Update Order Status ──────────────────────────────────────────────────
    @staticmethod
    def update_order_status(db: Session, order_id: int, data: OrderStatusUpdate):
        valid_statuses = {"PENDING", "PAID", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"}
        if data.status.upper() not in valid_statuses:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            )
        try:
            order = OrderRepository.update_order_status(db, order_id, data.status)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            return order
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    # ─── Cancel Order ─────────────────────────────────────────────────────────
    @staticmethod
    def cancel_order(db: Session, order_id: int):
        try:
            order = OrderRepository.cancel_order(db, order_id)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            return order
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    # ─── Order Status History ─────────────────────────────────────────────────
    @staticmethod
    def get_status_history(db: Session, order_id: int):
        order = OrderRepository.get_order_by_id(db, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return OrderRepository.get_order_status_history(db, order_id)

    # ─── Shipment ─────────────────────────────────────────────────────────────
    @staticmethod
    def create_shipment(db: Session, order_id: int, data: ShipmentCreate):
        order = OrderRepository.get_order_by_id(db, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        try:
            shipment = OrderRepository.create_shipment(db, order_id, data)
            # Also update order status to SHIPPED
            OrderRepository.update_order_status(db, order_id, "SHIPPED")
            return shipment
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_shipment_status(db: Session, tracking_number: str, data: ShipmentStatusUpdate):
        valid = {"SHIPPED", "OUT_FOR_DELIVERY", "DELIVERED"}
        if data.status.upper() not in valid:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid shipment status. Must be one of: {', '.join(valid)}"
            )
        try:
            shipment = OrderRepository.update_shipment_status(db, tracking_number, data.status)
            if not shipment:
                raise HTTPException(status_code=404, detail="Shipment not found")
            # If delivered, also update order status
            if data.status.upper() == "DELIVERED":
                OrderRepository.update_order_status(db, shipment.order_id, "DELIVERED")
            return shipment
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_shipment(db: Session, order_id: int):
        shipment = OrderRepository.get_shipment_by_order(db, order_id)
        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found for this order")
        return shipment

    # ─── Return Requests ──────────────────────────────────────────────────────
    @staticmethod
    def create_return_request(db: Session, user_id: int, data: ReturnRequestCreate):
        try:
            return OrderRepository.create_return_request(db, user_id, data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_all_return_requests(db: Session, status: Optional[str] = None):
        return OrderRepository.get_all_return_requests(db, status)

    @staticmethod
    def approve_return(db: Session, return_id: int, data: ReturnApprove):
        rr = OrderRepository.get_return_request_by_id(db, return_id)
        if not rr:
            raise HTTPException(status_code=404, detail="Return request not found")
        valid_methods = {"ORIGINAL_PAYMENT", "STORE_CREDIT", "BANK_TRANSFER"}
        if data.refund_method.upper() not in valid_methods:
            raise HTTPException(status_code=400, detail="Invalid refund method")
        try:
            return OrderRepository.approve_return_request(db, return_id, data.refund_method)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def complete_refund(db: Session, return_id: int):
        rr = OrderRepository.get_return_request_by_id(db, return_id)
        if not rr:
            raise HTTPException(status_code=404, detail="Return request not found")
        try:
            return OrderRepository.complete_refund(db, return_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    # ─── Analytics ────────────────────────────────────────────────────────────
    @staticmethod
    def get_top_selling(db: Session):
        return OrderRepository.get_top_selling_products(db)

    @staticmethod
    def get_return_requests_view(db: Session):
        return OrderRepository.get_return_requests_view(db)