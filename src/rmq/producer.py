import aio_pika
from aio_pika import Message

from src.rmq.logger import logger
from src.config import config


async def publish(
        message: str,
        routing_key: str = config.queue.name
) -> None:
    connection = await aio_pika.connect_robust(
        url=config.rmq.url
    )
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(
            name=routing_key,
            durable=config.queue.durable
        )
        await channel.default_exchange.publish(
            message=Message(body=message.encode("utf-8")),
            routing_key=queue.name
        )
        logger.info(f"[x] Sent message [{message!r}] for `{routing_key}`")
