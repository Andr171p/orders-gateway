from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class RMQLocalConfig(BaseSettings):
    host: str = os.getenv("RMQ_LOCAL_HOST")
    port: int = os.getenv("RMQ_LOCAL_PORT")
    url: str = f"amqp://{host}:{port}"


class RMQConfig(BaseSettings):
    host: str = os.getenv("RMQ_PUBLIC_HOST")
    port: str = os.getenv("RMQ_PUBLIC_PORT")
    url: str = f"amqp://{host}:{port}"


class QueueConfig(BaseSettings):
    name: str = "orders"
    durable: bool = False


class UvicornSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = "8000"


class AppConfig(BaseSettings):
    name: str = "orders-broadcast-API"


class Config(BaseSettings):
    app: AppConfig = AppConfig()
    rmq_local: RMQLocalConfig = RMQLocalConfig()
    rmq: RMQConfig = RMQConfig()
    queue: QueueConfig = QueueConfig()
    uvicorn: UvicornSettings = UvicornSettings()


config = Config()
