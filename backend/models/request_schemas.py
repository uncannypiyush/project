from pydantic import BaseModel
from typing import List, Optional

class IngestDocumentRequest(BaseModel):
    name: str
    content: str  # Raw content of the document

class QnARequest(BaseModel):
    query: str
    document_ids: Optional[List[int]] = None
