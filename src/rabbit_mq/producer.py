import logging

from aio_pika import Message, DeliveryMode

from typing import Dict, Any

from src.rabbit_mq.client import RabbitClient
from src.config import settings


log = logging.getLogger(__name__)


class RabbitProducer(RabbitClient):
    async def produce_message(
            self,
            body: str,
            headers: Dict[str, Any]
    ) -> None:
        exchange = await self.declare_exchange()
        message = Message(
            body=body.encode('utf-8'),
            headers=headers,
            delivery_mode=DeliveryMode.PERSISTENT
        )
        '''await self._channel.default_exchange.publish(
            message=message,
            routing_key=""
        )'''
        await exchange.publish(
            message=message,
            routing_key=""
        )
        print(body)
        log.warning("Published message: %s", body)
