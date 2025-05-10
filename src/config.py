from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class RabbitSettings(BaseSettings):
    user: str = os.getenv("RABBIT_USER")
    password: str = os.getenv("RABBIT_PASSWORD")
    host: str = os.getenv("RABBIT_HOST")
    port: str = os.getenv("RABBIT_PORT")

    url: str = f"amqp://{user}:{password}@{host}:{port}"

    queue_name: str = "orders"
    durable: bool = False


class UvicornSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = "8000"


class APISettings(BaseSettings):
    name: str = "orders-broadcast-API"


class Settings(BaseSettings):
    api: APISettings = APISettings()
    rabbit: RabbitSettings = RabbitSettings()
    uvicorn: UvicornSettings = UvicornSettings()


settings = Settings()
