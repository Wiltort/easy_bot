from pydantic import BaseModel
from beanie import Document


class Message(Document):
    text: str

    class Settings:
        name = "messages"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "message text"
                }
            ]
        }
    }

#может не пригодится
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
