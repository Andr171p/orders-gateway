from pydantic_settings import BaseSettings


class RMQConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5672


class QueueConfig(BaseSettings):
    name: str = "orders"
    durable: bool = False


class Config(BaseSettings):
    rmq: RMQConfig = RMQConfig()
    queue: QueueConfig = QueueConfig()


config = Config()
