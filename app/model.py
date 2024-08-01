from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "item": "Example schema!"
                }
            ]
        }
    }


class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "to do something good"
                }
            ]
        }
    }


class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {
                            "item": "Example schema 1!"
                        },
                        {
                            "item": "Example schema 2!"
                        }
                    ]
                }
            ]
        }
    }