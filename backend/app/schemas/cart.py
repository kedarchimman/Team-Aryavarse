from pydantic import BaseModel

class AddToCart(BaseModel):
    variant_id: int
    quantity: int