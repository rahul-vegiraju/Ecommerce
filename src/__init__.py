from fastapi import FastAPI
from src.orders.routes import order_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has stopped")

version = "v1"

app = FastAPI(
    title = "ecommerce",
    description= "A Rest API for a eco mmerce service",
    version = version,
    lifespan= life_span
)

app.include_router(order_router, prefix = f"/api/{version}/orders", tags=['orders'])