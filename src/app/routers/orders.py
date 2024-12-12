from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.app.schemas.order import OrderSchema, OrderResponse
from src.rmq import producer
from src.app import utils


orders_router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@orders_router.post(path='/push/', response_model=OrderResponse)
async def push_order(order: OrderSchema) -> JSONResponse | HTTPException:
    if order.project != "Дисконт Суши":
        return HTTPException(
            status_code=400,
            detail="Project != `Дисконт суши`"
        )
    message = utils.to_json(order.model_dump())
    await producer.publish(message=message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": "message sent successfully"
        }
    )
