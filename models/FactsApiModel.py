from pydantic import BaseModel

class ApiBaseModel(BaseModel):
    fact: str
    tokens_left: int
