from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.product_variant import ProductVariant


class ProductRepository:

    # -------- CREATE PRODUCT --------
    @staticmethod
    def create_product(db: Session, data):
        product = Product(
            name=data.name,
            description=data.description,
            category_id=data.category_id,
            sku=data.sku,
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    # -------- CREATE VARIANT --------
    @staticmethod
    def create_variant(db: Session, product_id: int, data):
        variant = ProductVariant(
            product_id=product_id,
            variant_name=data.variant_name,
            color=data.color,
            price=data.price,
            stock=data.stock,
            sku=data.sku
        )
        db.add(variant)
        db.commit()
        db.refresh(variant)
        return variant

    # -------- GET PRODUCTS --------
    @staticmethod
    def get_all_products(db: Session):
        return db.query(Product).filter(Product.is_deleted == False).all()

    # -------- UPDATE PRODUCT --------
    @staticmethod
    def update_product(db: Session, product_id: int, data):
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

        db.commit()
        db.refresh(product)
        return product

    # -------- SOFT DELETE PRODUCT --------
    @staticmethod
    def delete_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()

        if not product:
            return None

        product.is_deleted = True
        db.commit()
        return product

    # -------- UPDATE VARIANT --------
    @staticmethod
    def update_variant(db: Session, variant_id: int, data):
        variant = db.query(ProductVariant).filter(ProductVariant.id == variant_id).first()

        if not variant:
            return None

        if data.variant_name is not None:
            variant.variant_name = data.variant_name
        if data.color is not None:
            variant.color = data.color
        if data.price is not None:
            variant.price = data.price
        if data.stock is not None:
            variant.stock = data.stock
        if data.sku is not None:
            variant.sku = data.sku

        db.commit()
        db.refresh(variant)
        return variant

    # -------- DELETE VARIANT --------
    @staticmethod
    def delete_variant(db: Session, variant_id: int):
        variant = db.query(ProductVariant).filter(ProductVariant.id == variant_id).first()

        if not variant:
            return None

        db.delete(variant)
        db.commit()
        return variant