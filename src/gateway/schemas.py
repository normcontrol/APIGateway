from pydantic import BaseModel


class Document(BaseModel):
    owner: str
    time: str
    content: dict