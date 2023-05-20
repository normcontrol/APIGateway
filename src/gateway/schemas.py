from pydantic import BaseModel


class Document(BaseModel):
    owner: str
    time: str
    page_count: int
    content: dict

class DocumentData(BaseModel):
    document_type: str
    document_id: str


class AllData(BaseModel):
    document_type: str
    path: str
    document_id: int
    gost: str