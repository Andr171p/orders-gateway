from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.schemas.order import OrderSchema


orders_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@orders_router.post(path='/push/', response_model=...)
async def push_order(order: OrderSchema) -> JSONResponse:
    ...
