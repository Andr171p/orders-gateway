from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.rmq.message import create_message
from src.rmq import producer
from src.api_v1.schemas.order import OrderSchema, OrderResponse
from src.api_v1 import utils


orders_router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@orders_router.post(path='/push/', response_model=OrderResponse)
async def push_order(order: OrderSchema) -> JSONResponse | HTTPException:
    project: str = order.project
    body: str = utils.to_json(order.model_dump())
    message = create_message(
        body=body,
        project=project
    )
    await producer.publish(message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": "message sent successfully to ..."
        }
    )
