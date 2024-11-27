from pydantic_settings import BaseSettings


class RMQConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5672


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
    rmq: RMQConfig = RMQConfig()
    queue: QueueConfig = QueueConfig()
    uvicorn: UvicornSettings = UvicornSettings()


config = Config()
