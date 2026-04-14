from sqlalchemy.orm import Session
from app.repositories.product_repo import ProductRepository


class ProductService:

    @staticmethod
    def create_product(db: Session, data):
        return ProductRepository.create_product(db, data)

    @staticmethod
    def create_variant(db: Session, product_id: int, data):
        return ProductRepository.create_variant(db, product_id, data)

    @staticmethod
    def get_products(db: Session):
        return ProductRepository.get_all_products(db)

    @staticmethod
    def update_product(db: Session, product_id: int, data):
        return ProductRepository.update_product(db, product_id, data)

    @staticmethod
    def delete_product(db: Session, product_id: int):
        return ProductRepository.delete_product(db, product_id)

    @staticmethod
    def update_variant(db: Session, variant_id: int, data):
        return ProductRepository.update_variant(db, variant_id, data)

    @staticmethod
    def delete_variant(db: Session, variant_id: int):
        return ProductRepository.delete_variant(db, variant_id)