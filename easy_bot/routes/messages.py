from fastapi import APIRouter
from ..models.messages import Message
from beanie import PydanticObjectId
from ..database.connection import Database
from typing import List

api_router = APIRouter()
message_database = Database(Message)


@api_router.post("/messages", status_code=201)
async def add_message(mes: Message) -> dict:
    await message_database.save(mes)
    return {"message": "Message added successfully"}


@api_router.get("/messages", response_model=List[Message])
async def retrieve_messages() -> List[Message]:
    messages = await message_database.get_all()
    return messages
