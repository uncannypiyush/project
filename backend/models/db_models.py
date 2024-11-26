from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Document(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True  # Allows direct mapping from ORM objects


class DocumentEmbedding(BaseModel):
    id: int
    document_name: str
    chunk_id: str
    content: str
    embedding: list[float]
    created_at: datetime

    class Config:
        orm_mode = True
