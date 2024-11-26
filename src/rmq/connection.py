import aio_pika
from aio_pika.abc import AbstractQueue
from aio_pika.abc import AbstractRobustConnection
from aio_pika.abc import AbstractRobustChannel
from aio_pika.abc import AbstractTransaction
from typing import AsyncGenerator, Optional
import contextlib

from src.config import config


class RMQConnection:
    def __init__(
            self,
            host: str = config.rmq.host,
            port: int = config.rmq.port
    ) -> None:
        self._url: str = f"amqp://{host}:{port}/"
        self._connection: Optional[AbstractRobustConnection] = None
        self._channel: Optional[AbstractRobustChannel] = None

    async def connect(self) -> None:
        if not self._connection or self._connection.is_closed:
            self._connection = await aio_pika.connect_robust(
                url=self._url
            )
            self._channel = await self._connection.channel()

    async def close(self) -> None:
        if self._connection or not self._connection.is_closed:
            await self._connection.close()
            self._connection = None
            self._channel = None

    async def create_queue(self) -> AbstractQueue:
        queue: AbstractQueue = await self._channel.declare_queue(
            name=config.queue.name,
            durable=config.queue.durable
        )
        return queue

    @contextlib.asynccontextmanager
    async def transaction(self) -> AsyncGenerator[AbstractTransaction]:
        await self.connect()
        async with self._connection:
            async with self._channel.transaction():
                yield
