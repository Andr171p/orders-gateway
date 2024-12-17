from fastapi import FastAPI
from contextlib import AbstractAsyncContextManager

from src.api_v1.middlewares.globals import g


async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    yield
