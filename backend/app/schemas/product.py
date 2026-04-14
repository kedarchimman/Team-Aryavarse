from pydantic import BaseModel
from typing import Optional


# -------- PRODUCT --------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int
    sku: Optional[str] = None


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    sku: Optional[str] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    category_id: int
    sku: Optional[str]
    is_deleted: bool

    class Config:
        from_attributes = True


# -------- VARIANT --------
class VariantCreate(BaseModel):
    variant_name: str
    price: float
    stock: int
    color: str
    sku: Optional[str] = None


class VariantUpdate(BaseModel):
    variant_name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    color: Optional[str] = None
    sku: Optional[str] = None