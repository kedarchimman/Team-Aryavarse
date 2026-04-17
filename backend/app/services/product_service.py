from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.product_repo import ProductRepository
from app.schemas.product import (
    ProductCreate, ProductUpdate,
    VariantCreate, VariantUpdate,
    CategoryCreate, CategoryUpdate,
    ColorCreate, ProductImageCreate
)


class ProductService:

    # ─── Categories ───────────────────────────────────────────────────────────
    @staticmethod
    def get_all_categories(db: Session):
        return ProductRepository.get_all_categories(db)

    @staticmethod
    def get_category(db: Session, category_id: int):
        category = ProductRepository.get_category_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    @staticmethod
    def create_category(db: Session, data: CategoryCreate):
        return ProductRepository.create_category(db, data)

    @staticmethod
    def update_category(db: Session, category_id: int, data: CategoryUpdate):
        category = ProductRepository.update_category(db, category_id, data)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    @staticmethod
    def delete_category(db: Session, category_id: int):
        category = ProductRepository.delete_category(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return {"message": "Category deleted"}

    # ─── Colors ───────────────────────────────────────────────────────────────
    @staticmethod
    def get_all_colors(db: Session):
        return ProductRepository.get_all_colors(db)

    @staticmethod
    def create_color(db: Session, data: ColorCreate):
        return ProductRepository.create_color(db, data)

    # ─── Products ─────────────────────────────────────────────────────────────
    @staticmethod
    def create_product(db: Session, data: ProductCreate, user_id: int):
        return ProductRepository.create_product(db, data, user_id)

    @staticmethod
    def get_products(db: Session, category_id=None, is_active=None):
        return ProductRepository.get_all_products(db, category_id, is_active)

    @staticmethod
    def get_product(db: Session, product_id: int):
        product = ProductRepository.get_product_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        variants = ProductRepository.get_variants_by_product(db, product_id)
        images = ProductRepository.get_images_by_product(db, product_id)
        return product, variants, images

    @staticmethod
    def update_product(db: Session, product_id: int, data: ProductUpdate, user_id: int):
        product = ProductRepository.update_product(db, product_id, data, user_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    @staticmethod
    def delete_product(db: Session, product_id: int):
        product = ProductRepository.delete_product(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted successfully"}

    # ─── Variants ─────────────────────────────────────────────────────────────
    @staticmethod
    def create_variant(db: Session, product_id: int, data: VariantCreate, user_id: int):
        product = ProductRepository.get_product_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductRepository.create_variant(db, product_id, data, user_id)

    @staticmethod
    def get_variants(db: Session, product_id: int):
        return ProductRepository.get_variants_by_product(db, product_id)

    @staticmethod
    def update_variant(db: Session, variant_id: int, data: VariantUpdate, user_id: int):
        variant = ProductRepository.update_variant(db, variant_id, data, user_id)
        if not variant:
            raise HTTPException(status_code=404, detail="Variant not found")
        return variant

    @staticmethod
    def delete_variant(db: Session, variant_id: int):
        variant = ProductRepository.delete_variant(db, variant_id)
        if not variant:
            raise HTTPException(status_code=404, detail="Variant not found")
        return {"message": "Variant deleted successfully"}

    # ─── Images ───────────────────────────────────────────────────────────────
    @staticmethod
    def add_image(db: Session, product_id: int, data: ProductImageCreate):
        product = ProductRepository.get_product_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductRepository.add_product_image(db, product_id, data)

    @staticmethod
    def delete_image(db: Session, image_id: int):
        img = ProductRepository.delete_product_image(db, image_id)
        if not img:
            raise HTTPException(status_code=404, detail="Image not found")
        return {"message": "Image deleted"}

    # ─── Low Stock ────────────────────────────────────────────────────────────
    @staticmethod
    def get_low_stock(db: Session):
        return ProductRepository.get_low_stock_variants(db)