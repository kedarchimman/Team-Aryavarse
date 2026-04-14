from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.checkout_route import router as checkout_router

app = FastAPI()

print(" MAIN.PY LOADED")

# ADD CORS FIRST (before routers)
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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  IMPORT ROUTERS AFTER middleware
from app.routes import cart, products
from app.api import wishlist

app.include_router(cart.router)
app.include_router(products.router)
app.include_router(wishlist.router)
app.include_router(checkout_router)