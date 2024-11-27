from aio_pika import Message

from src.rmq.connection import RMQConnection
from src.config import config


class RMQProducer(RMQConnection):
    async def publish(self, body: bytes) -> None:
        async with self.transaction():
            await self._channel.default_exchange.publish(
                message=Message(body=body),
                routing_key=config.queue.name,
            )
