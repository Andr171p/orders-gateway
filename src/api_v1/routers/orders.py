from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.rabbit_mq.publish import publish
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
    headers = {
        "project": project
    }
    await publish(
        body=body,
        headers=headers
    )
    return JSONResponse(
        content={
            "status": "ok",
            "data": f"message sent successfully to {project}"
        }
    )
