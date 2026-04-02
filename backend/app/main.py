from fastapi import FastAPI
from app.api.routes.cart import router as cart_router
from app.api.routes.products import router as product_router
from app.api.routes.wishlist import router as wishlist_router

from app.db.session import engine
from app.db.base import Base
from app.db import base  # ✅ ensures all models are loaded


# ✅ Create tables (only for development)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="E-commerce Backend API",
    version="1.0.0"
)


# Register routers
app.include_router(cart_router)
app.include_router(product_router)
app.include_router(wishlist_router)


@app.get("/")
def home():
    return {
        "message": "E-commerce backend running",
        "status": "OK"
    }