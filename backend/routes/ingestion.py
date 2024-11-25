from fastapi import APIRouter, UploadFile, HTTPException
from services.embeddings import generate_embeddings, store_embeddings
import asyncio

router = APIRouter()

@router.post("/")
async def ingest_document(file: UploadFile):
    try:
        content = (await file.read()).decode("utf-8")
        chunks = [content[i:i+512] for i in range(0, len(content), 512)]

        embeddings = await asyncio.gather(*[generate_embeddings(chunk) for chunk in chunks])

        await store_embeddings(file.filename, chunks, embeddings)
        return {"message": "Document ingested successfully", "chunks_processed": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
