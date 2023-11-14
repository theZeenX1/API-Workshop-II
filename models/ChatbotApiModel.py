from pydantic import BaseModel

class ApiBaseModel(BaseModel):
    assistant: str
    tokens_left: int