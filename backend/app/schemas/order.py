from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from datetime import date


# ─── Order Status Update ──────────────────────────────────────────────────────
class OrderStatusUpdate(BaseModel):
    status: str                         # PENDING | PAID | PROCESSING | SHIPPED | DELIVERED | CANCELLED


# ─── Order Item Out ───────────────────────────────────────────────────────────
class OrderItemOut(BaseModel):
    id: int
    order_id: int
    variant_id: int
    quantity: int
    price: Decimal

    class Config:
        from_attributes = True


# ─── Order Out ────────────────────────────────────────────────────────────────
class OrderOut(BaseModel):
    id: int
    user_id: Optional[int] = None
    total_amount: Decimal
    status: str
    payment_status: str
    address_id: Optional[int] = None

    class Config:
        from_attributes = True


class OrderDetailOut(OrderOut):
    items: List[OrderItemOut] = []


# ─── Order Status History Out ─────────────────────────────────────────────────
class OrderStatusHistoryOut(BaseModel):
    id: int
    order_id: int
    status: str
    changed_by: Optional[int] = None
    remarks: Optional[str] = None

    class Config:
        from_attributes = True


# ─── Shipment ─────────────────────────────────────────────────────────────────
class ShipmentCreate(BaseModel):
    courier_name: str
    tracking_number: str
    estimated_delivery: Optional[date] = None


class ShipmentStatusUpdate(BaseModel):
    status: str                         # SHIPPED | OUT_FOR_DELIVERY | DELIVERED


class ShipmentOut(BaseModel):
    id: int
    order_id: int
    courier_name: str
    tracking_number: str
    shipment_status: str
    tracking_url: Optional[str] = None
    estimated_delivery: Optional[date] = None

    class Config:
        from_attributes = True


# ─── Return Request ───────────────────────────────────────────────────────────
class ReturnRequestCreate(BaseModel):
    order_id: int
    order_item_id: int
    quantity: int
    reason: str


class ReturnApprove(BaseModel):
    refund_method: str                  # ORIGINAL_PAYMENT | STORE_CREDIT | BANK_TRANSFER


class ReturnRequestOut(BaseModel):
    id: int
    order_id: int
    order_item_id: int
    user_id: int
    quantity: int
    reason: str
    status: str
    refund_amount: Optional[Decimal] = None
    refund_method: Optional[str] = None

    class Config:
        from_attributes = True