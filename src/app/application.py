from fastapi import FastAPI
from contextlib import AbstractAsyncContextManager

from src.app.middlewares.globals import g
from src.rmq.producer import RMQProducer


async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    producer = RMQProducer()
    g.set_default("producer", producer)
    yield
    del producer
