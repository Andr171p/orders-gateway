from fastapi import FastAPI
from contextlib import AbstractAsyncContextManager

from src.app.middlewares.globals import g


async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    yield
