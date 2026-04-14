from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    VariantCreate,
    VariantUpdate
)
from app.services.product_service import ProductService
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/admin/products", tags=["Admin Products"])


# -------- CREATE PRODUCT --------
@router.post("/")
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return ProductService.create_product(db, data)


# -------- CREATE VARIANT --------
@router.post("/{product_id}/variant")
def create_variant(
    product_id: int,
    data: VariantCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return ProductService.create_variant(db, product_id, data)


# -------- GET PRODUCTS --------
@router.get("/")
def get_products(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return ProductService.get_products(db)


# -------- UPDATE PRODUCT --------
@router.put("/{product_id}")
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = ProductService.update_product(db, product_id, data)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# -------- DELETE PRODUCT --------
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = ProductService.delete_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}


# -------- UPDATE VARIANT --------
@router.put("/variant/{variant_id}")
def update_variant(
    variant_id: int,
    data: VariantUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    variant = ProductService.update_variant(db, variant_id, data)

    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    return variant


# -------- DELETE VARIANT --------
@router.delete("/variant/{variant_id}")
def delete_variant(
    variant_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    variant = ProductService.delete_variant(db, variant_id)

    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    return {"message": "Variant deleted successfully"}