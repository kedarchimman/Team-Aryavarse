from fastapi import FastAPI
from app.api.routes.cart import router as cart_router

app = FastAPI()

app.include_router(cart_router)


@app.get("/")
def home():
    return {"message": "FastAPI cart backend running"}