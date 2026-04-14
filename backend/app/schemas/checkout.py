from typing import Optional
from pydantic import BaseModel, Field, field_validator


class CheckoutRequest(BaseModel):
    user_id: int = Field(..., gt=0)
    address_id: int = Field(..., gt=0)
    coupon_code: Optional[str] = None
    shipping_charge: float = Field(default=0, ge=0)
    tax_amount: float = Field(default=0, ge=0)
    platform_fee: float = Field(default=0, ge=0)
    discount_amount: float = Field(default=0, ge=0)

    @field_validator("coupon_code")
    @classmethod
    def normalize_coupon(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        value = value.strip().upper()
        return value if value else None


class PaymentRequest(BaseModel):
    order_id: int = Field(..., gt=0)
    payment_method: str = Field(..., min_length=2, max_length=50)
    payment_status: str = Field(..., min_length=2, max_length=20)
    transaction_ref: str = Field(..., min_length=2, max_length=100)

    @field_validator("payment_method")
    @classmethod
    def normalize_payment_method(cls, value: str) -> str:
        return value.strip().upper()

    @field_validator("payment_status")
    @classmethod
    def validate_payment_status(cls, value: str) -> str:
        value = value.strip().upper()
        allowed = {"SUCCESS", "FAILED", "PENDING"}
        if value not in allowed:
            raise ValueError(f"payment_status must be one of {allowed}")
        return value

    @field_validator("transaction_ref")
    @classmethod
    def normalize_transaction_ref(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("transaction_ref cannot be empty")
        return value