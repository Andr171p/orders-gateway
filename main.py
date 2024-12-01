from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.routers.orders import orders_router
from src.app.middlewares.globals import GlobalMiddleware
from src.app.application import lifespan
from src.config import config


app = FastAPI(
    title=config.app.name,
    redirect_slashes=False
    # lifespan=lifespan
)

app.include_router(orders_router)

app.add_middleware(GlobalMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
