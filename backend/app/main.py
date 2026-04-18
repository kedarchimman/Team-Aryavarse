from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.cart import router as cart_router
from app.api.routes.products import router as products_router

from app.api.routes.wishlist import router as wishlist_router


app = FastAPI()

print("MAIN.PY LOADED")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:9000",
        "http://localhost:9001",
        "http://127.0.0.1:9000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.1.11:9001",
    ],
)
from fastapi import FastAPI, Depends
from app.api.routes import auth
from app.api.routes import test_auth
from app.db.session import get_db
from fastapi.middleware.cors import CORSMiddleware
from app.db import base_class  # 🔥 THIS FIXES EVERYTHING
app = FastAPI(title="Healthcare Backend")

# ─── Routers ─────────────────────────────────────────────
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(test_auth.router, prefix="/test", tags=["Test"])


# ─── Quick DB health check ────────────────────────────────
@app.get("/test/db", tags=["Test"])
def test_db(db=Depends(get_db)):
    return {"message": "DB connected"}


# ─── Root ─────────────────────────────────────────────────
@app.get("/", tags=["Root"])
def root():
    return {"message": "Healthcare API is running"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cart_router)
app.include_router(products_router)
app.include_router(wishlist_router)

from app.api.routes.admin import (
    dashboard,
    product_admin,
    order_admin,
    payment_admin,
    support_admin,
    inventory_admin
)

app.include_router(dashboard.router)
app.include_router(product_admin.router)
app.include_router(order_admin.router)
app.include_router(payment_admin.router)
app.include_router(support_admin.router)
app.include_router(inventory_admin.router)

