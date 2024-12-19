from typing import Dict, Any

from src.rabbit_mq.producer import RabbitProducer


async def publish(
        body: str,
        headers: Dict[str, Any]
) -> None:
    async with RabbitProducer() as producer:
        await producer.produce_message(
            body=body,
            headers=headers
        )
