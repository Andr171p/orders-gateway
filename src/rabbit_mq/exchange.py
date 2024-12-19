from typing import TYPE_CHECKING

from aio_pika import ExchangeType

from src.rabbit_mq.exc import RabbitException
from src.config import settings


if TYPE_CHECKING:
    from aio_pika.abc import AbstractRobustChannel


class RabbitExchange:
    _channel: "AbstractRobustChannel"

    async def declare_exchange(self) -> None:
        if self._channel is None:
            raise RabbitException("Channel must initialized first")
        await self._channel.declare_exchange(
            name=settings.rabbit.queue_name,
            type=ExchangeType.FANOUT
        )
