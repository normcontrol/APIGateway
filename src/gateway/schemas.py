from pydantic import BaseModel


class Document(BaseModel):
    owner: str
    time: str
    content: dict

class DocumentData(BaseModel):
    document_type: str
    path: str

class AllData(BaseModel):
    document_type: str
    path: str
    gost: str