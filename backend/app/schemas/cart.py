from pydantic import BaseModel
from typing import Optional


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    user_id: Optional[int] = None
    guest_id: Optional[str] = None   


class UpdateCartRequest(BaseModel):
    cart_item_id: int
    quantity: int


class MergeGuestCartRequest(BaseModel):
    guest_id: str   
    user_id: int