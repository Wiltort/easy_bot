from fastapi import FastAPI
from easy_bot.routes.messages import api_router
from easy_bot.database.connection import init

app = FastAPI()


@app.on_event("startup")
async def db_init():
    await init()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

app.include_router(api_router, prefix='/api/v1')
