from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api_v1.routers.orders import orders_router
from src.api_v1.middlewares.globals import GlobalMiddleware
from src.config import settings


app = FastAPI(
    title=settings.api.name,
    redirect_slashes=False
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
