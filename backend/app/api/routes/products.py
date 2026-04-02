from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from app.core.dependencies import get_db
from app.services.product_service import advanced_search_products

router = APIRouter(prefix="/products", tags=["Products"])


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    is_active: bool
    category: Optional[str] = None
    color: Optional[str] = None
    size: Optional[str] = None
    is_recommended: bool

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[ProductResponse]


@router.get("/search", response_model=ProductListResponse)
def search_products(
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    category: Optional[List[str]] = Query(None),
    color: Optional[List[str]] = Query(None),
    size: Optional[List[str]] = Query(None),
    in_stock: Optional[bool] = None,
    sort_by: str = "relevance",
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return advanced_search_products(
        db=db,
        search=search,
        min_price=min_price,
        max_price=max_price,
        category=category,
        color=color,
        size=size,
        in_stock=in_stock,
        sort_by=sort_by,
        page=page,
        limit=limit
    )