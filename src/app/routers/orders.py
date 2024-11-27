from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.schemas.order import OrderSchema, OrderResponse
from src.app.middlewares.globals import g
from src.app import utils


orders_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@orders_router.post(path='/push/', response_model=OrderResponse)
async def push_order(order: OrderSchema) -> JSONResponse:
    message = utils.to_json(order.model_dump())
    producer = g.producer
    await producer.publish(body=message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": "message sent successfully"
        }
    )
