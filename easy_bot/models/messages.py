from pydantic import BaseModel
from beanie import Document


class Message(Document):
    author: str
    text: str

    class Settings:
        name = "messages"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "author": "author username",
                    "text": "message text"
                }
            ]
        }
    }


class MessageCreate(BaseModel):
    text: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "message text"
                }
            ]
        }
    }
