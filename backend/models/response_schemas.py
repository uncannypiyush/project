from pydantic import BaseModel
from typing import List, Optional

class IngestDocumentResponse(BaseModel):
    message: str
    chunks: int  # Number of document chunks processed

class QnAResponse(BaseModel):
    answer: str
    context: List[str]  # Relevant document chunks used for generating the answer

class ToggleDocumentResponse(BaseModel):
    message: str
    document_id: int
    new_status: bool  # Updated status of the document (active or inactive)
