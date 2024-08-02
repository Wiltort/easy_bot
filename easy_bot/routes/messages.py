from fastapi import APIRouter, Request
from models.messages import Message, MessageCreate
from database.connection import Database
from typing import List

api_router = APIRouter()
message_database = Database(Message)


@api_router.post("/messages", status_code=201)
async def add_message(mes: MessageCreate, request=Request) -> dict:
    author = "Anonimous"
    new_mes = Message(author=author, text=mes.text)
    await message_database.save(new_mes)
    return {"message": "Message added successfully"}


@api_router.get("/messages", response_model=List[Message])
async def retrieve_messages() -> List[Message]:
    messages = await message_database.get_all()
    return messages

