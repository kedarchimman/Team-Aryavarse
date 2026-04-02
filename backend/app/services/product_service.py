from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.product import Product
from app.models.category import Category
from app.models.product_variant import ProductVariant


def advanced_search_products(
    db: Session,
    search=None,
    min_price=None,
    max_price=None,
    category=None,
    color=None,
    size=None,
    in_stock=None,
    sort_by="relevance",
    page=1,
    limit=10
):
    query = (
        db.query(
            Product.id.label("id"),
            Product.name.label("name"),
            Product.price.label("price"),
            Product.stock.label("stock"),
            Product.is_active.label("is_active"),
            Category.name.label("category"),
            ProductVariant.color.label("color"),
            ProductVariant.size.label("size"),
            Product.is_recommended.label("is_recommended")
        )
        .outerjoin(Category, Product.category_id == Category.id)
        .outerjoin(ProductVariant, Product.id == ProductVariant.product_id)
    )

    if search:
        query = query.filter(
            or_(
                Product.name.ilike(f"%{search}%"),
                Category.name.ilike(f"%{search}%"),
                ProductVariant.color.ilike(f"%{search}%"),
                ProductVariant.size.ilike(f"%{search}%")
            )
        )

    if min_price is not None:
        query = query.filter(Product.price >= min_price)

    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    if category:
        query = query.filter(Category.name.in_(category))

    if color:
        query = query.filter(ProductVariant.color.in_(color))

    if size:
        query = query.filter(ProductVariant.size.in_(size))

    if in_stock is not None:
        if in_stock:
            query = query.filter(Product.stock > 0)
        else:
            query = query.filter(Product.stock <= 0)

    if sort_by == "price_low":
        query = query.order_by(Product.price.asc())
    elif sort_by == "price_high":
        query = query.order_by(Product.price.desc())
    elif sort_by == "newest":
        query = query.order_by(Product.id.desc())
    else:
        query = query.order_by(Product.is_recommended.desc(), Product.id.desc())

    offset = (page - 1) * limit

    total = query.distinct(Product.id, ProductVariant.color, ProductVariant.size).count()
    rows = query.distinct(Product.id, ProductVariant.color, ProductVariant.size).offset(offset).limit(limit).all()

    data = []
    for row in rows:
        data.append({
            "id": row.id,
            "name": row.name,
            "price": float(row.price) if row.price is not None else 0.0,
            "stock": row.stock,
            "is_active": row.is_active,
            "category": row.category,
            "color": row.color,
            "size": row.size,
            "is_recommended": row.is_recommended
        })

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": data
    }