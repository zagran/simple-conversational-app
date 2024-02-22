import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    LLM_MODEL_PATH: str = "/models/current.gguf"


class TestConfig(Config): ...


class LocalConfig(Config):
    LLM_MODEL_PATH: str = "/models/synthia-7b-v2.0-16k.Q2_K.gguf"


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
