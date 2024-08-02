from os import getenv
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any
from pydantic_settings import BaseSettings
from models.messages import Message


URI = getenv("DATABASE_URL")


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Message,]
        )

    class Config:
        env_file = ".env"


async def init():
    client = AsyncIOMotorClient(URI)
    await init_beanie(
        database=client.mes_db,
        document_models=[Message,]
    )


class Database:

    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get_all(self) -> Any:
        docs = await self.model.find_all().to_list()
        return docs
