import logging
import sys
from os import getenv
from dotenv import load_dotenv

from fastapi import FastAPI
from routes.messages import api_router, retrieve_messages
from database.connection import init
from aiogram import Bot, Dispatcher, html, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from contextlib import asynccontextmanager
from models import messages
from database.connection import Database


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    url_webhook = getenv("WEBHOOK_URL")
    await bot.set_webhook(url=url_webhook,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)
message_database = Database(messages.Message)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def send_and_save_message(message: Message) -> None:
    author = message.from_user.username
    text = message.text
    new_message = messages.Message(author=author, text=text)
    await message_database.save(new_message)


@dp.message(Command(commands=["messages"]))
async def show_messages(message: types.Message):
    messages = await retrieve_messages()
    text = "\n".join(
        f"**{message['author']}**: {message['content']}"
        for message in messages.messages
        )
    await message.reply(text)


@app.on_event("startup")
async def db_init():
    await init()


@app.post("/webhook")
async def webhook_handler(update: dict):
    try:
        update = types.Update.to_object(update)
        await dp.process_update(update)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": str(e)}


app.include_router(api_router, prefix='/api/v1')


if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5000,
        reload=True,
    )
