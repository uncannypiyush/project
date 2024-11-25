from fastapi import APIRouter, Query, HTTPException
from services.embeddings import retrieve_relevant_chunks
from utils.cache import cache_query
import openai

router = APIRouter()

@router.get("/")
async def qna(query: str, document_ids: list[int] = Query(None)):
    try:
        # Check cache
        cached_result = await cache_query(query)
        if cached_result:
            return {"answer": cached_result}

        # Retrieve relevant chunks
        chunks = await retrieve_relevant_chunks(query, document_ids)

        # Generate answer using RAG
        context = "\n".join(chunks)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the question based on the context:\n{context}\n\nQuestion: {query}",
            max_tokens=150,
        )
        answer = response.choices[0].text.strip()

        # Cache the result
        await cache_query(query, answer)

        return {"answer": answer, "context": chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing Q&A: {str(e)}")
