from fastapi import FastAPI

from src.app.routers.orders import orders_router
from src.app.middlewares.globals import GlobalMiddleware
from src.app.application import lifespan
from src.config import config


app = FastAPI(
    title=config.app.name,
    lifespan=lifespan
)

app.include_router(orders_router)

app.add_middleware(GlobalMiddleware)
