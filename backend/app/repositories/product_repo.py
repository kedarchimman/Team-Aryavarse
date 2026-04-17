from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.product_image import ProductImage
from app.models.category import Category
from app.models.color import Color
from typing import Optional


class ProductRepository:

    # ─── Category ─────────────────────────────────────────────────────────────
    @staticmethod
    def get_all_categories(db: Session):
        return db.query(Category).filter(Category.is_deleted == False).all()

    @staticmethod
    def get_category_by_id(db: Session, category_id: int):
        return db.query(Category).filter(
            Category.id == category_id,
            Category.is_deleted == False
        ).first()

    @staticmethod
    def create_category(db: Session, data):
        category = Category(
            name=data.name,
            description=data.description,
            is_active=data.is_active if data.is_active is not None else True
        )
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def update_category(db: Session, category_id: int, data):
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        if data.name is not None:
            category.name = data.name
        if data.description is not None:
            category.description = data.description
        if data.is_active is not None:
            category.is_active = data.is_active
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def delete_category(db: Session, category_id: int):
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        category.is_deleted = True
        db.commit()
        return category

    # ─── Colors ───────────────────────────────────────────────────────────────
    @staticmethod
    def get_all_colors(db: Session):
        return db.query(Color).filter(Color.is_active == True).all()

    @staticmethod
    def create_color(db: Session, data):
        color = Color(name=data.name, hex_code=data.hex_code, is_active=True)
        db.add(color)
        db.commit()
        db.refresh(color)
        return color

    # ─── Product ──────────────────────────────────────────────────────────────
    @staticmethod
    def create_product(db: Session, data, user_id: int):
        product = Product(
            name=data.name,
            description=data.description,
            category_id=data.category_id,
            sku=data.sku,
            is_active=data.is_active if data.is_active is not None else True,
            details_and_fit=data.details_and_fit,
            fabric_and_care=data.fabric_and_care,
            return_and_exchange=data.return_and_exchange,
            tax_rate_id=data.tax_rate_id,
            created_by=user_id,
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all_products(db: Session, category_id: Optional[int] = None, is_active: Optional[bool] = None):
        query = db.query(Product).filter(Product.is_deleted == False)
        if category_id is not None:
            query = query.filter(Product.category_id == category_id)
        if is_active is not None:
            query = query.filter(Product.is_active == is_active)
        return query.all()

    @staticmethod
    def get_product_by_id(db: Session, product_id: int):
        return db.query(Product).filter(
            Product.id == product_id,
            Product.is_deleted == False
        ).first()

    @staticmethod
    def update_product(db: Session, product_id: int, data, user_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        if data.name is not None:
            product.name = data.name
        if data.description is not None:
            product.description = data.description
        if data.category_id is not None:
            product.category_id = data.category_id
        if data.sku is not None:
            product.sku = data.sku
        if data.is_active is not None:
            product.is_active = data.is_active
        if data.details_and_fit is not None:
            product.details_and_fit = data.details_and_fit
        if data.fabric_and_care is not None:
            product.fabric_and_care = data.fabric_and_care
        if data.return_and_exchange is not None:
            product.return_and_exchange = data.return_and_exchange
        if data.tax_rate_id is not None:
            product.tax_rate_id = data.tax_rate_id
        product.updated_by = user_id
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        product.is_deleted = True
        db.commit()
        return product

    # ─── Variant ──────────────────────────────────────────────────────────────
    @staticmethod
    def create_variant(db: Session, product_id: int, data, user_id: int):
        variant = ProductVariant(
            product_id=product_id,
            variant_name=data.variant_name,
            price=data.price,
            stock=data.stock if data.stock is not None else 0,
            sku=data.sku,
            color=data.color,
            color_id=data.color_id,
            size=data.size,
            low_stock_threshold=data.low_stock_threshold if data.low_stock_threshold is not None else 5,
            created_by=user_id,
        )
        db.add(variant)
        db.commit()
        db.refresh(variant)
        return variant

    @staticmethod
    def get_variants_by_product(db: Session, product_id: int):
        return db.query(ProductVariant).filter(
            ProductVariant.product_id == product_id,
            ProductVariant.is_deleted == False
        ).all()

    @staticmethod
    def get_variant_by_id(db: Session, variant_id: int):
        return db.query(ProductVariant).filter(
            ProductVariant.id == variant_id,
            ProductVariant.is_deleted == False
        ).first()

    @staticmethod
    def update_variant(db: Session, variant_id: int, data, user_id: int):
        variant = db.query(ProductVariant).filter(ProductVariant.id == variant_id).first()
        if not variant:
            return None
        if data.variant_name is not None:
            variant.variant_name = data.variant_name
        if data.price is not None:
            variant.price = data.price
        if data.stock is not None:
            variant.stock = data.stock
        if data.sku is not None:
            variant.sku = data.sku
        if data.color is not None:
            variant.color = data.color
        if data.color_id is not None:
            variant.color_id = data.color_id
        if data.size is not None:
            variant.size = data.size
        if data.low_stock_threshold is not None:
            variant.low_stock_threshold = data.low_stock_threshold
        if data.is_deleted is not None:
            variant.is_deleted = data.is_deleted
        variant.updated_by = user_id
        db.commit()
        db.refresh(variant)
        return variant

    @staticmethod
    def delete_variant(db: Session, variant_id: int):
        variant = db.query(ProductVariant).filter(ProductVariant.id == variant_id).first()
        if not variant:
            return None
        variant.is_deleted = True
        db.commit()
        return variant

    # ─── Images ───────────────────────────────────────────────────────────────
    @staticmethod
    def add_product_image(db: Session, product_id: int, data):
        # If is_primary = True, call the stored procedure
        if data.is_primary:
            db.execute(
                text("CALL sp_add_product_image(:pid, :url, :name, :primary)"),
                {"pid": product_id, "url": data.image_url, "name": data.image_name, "primary": True}
            )
            db.commit()
            return db.query(ProductImage).filter(
                ProductImage.product_id == product_id,
                ProductImage.is_primary == True
            ).first()
        else:
            img = ProductImage(
                product_id=product_id,
                image_url=data.image_url,
                image_name=data.image_name,
                is_primary=False
            )
            db.add(img)
            db.commit()
            db.refresh(img)
            return img

    @staticmethod
    def get_images_by_product(db: Session, product_id: int):
        return db.query(ProductImage).filter(
            ProductImage.product_id == product_id
        ).all()

    @staticmethod
    def delete_product_image(db: Session, image_id: int):
        img = db.query(ProductImage).filter(ProductImage.id == image_id).first()
        if not img:
            return None
        db.delete(img)
        db.commit()
        return img

    # ─── Low Stock ────────────────────────────────────────────────────────────
    @staticmethod
    def get_low_stock_variants(db: Session):
        result = db.execute(text("SELECT * FROM low_stock_products"))
        return result.mappings().all()