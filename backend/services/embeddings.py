from sentence_transformers import SentenceTransformer
import asyncpg

model = SentenceTransformer("all-MiniLM-L6-v2")

async def generate_embeddings(text: str):
    return model.encode([text])[0]

async def store_embeddings(doc_name, chunks, embeddings):
    db = await asyncpg.connect("postgresql://user:password@localhost/dbname")
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        await db.execute(
            """
            INSERT INTO document_embeddings (document_name, chunk_id, content, embedding)
            VALUES ($1, $2, $3, $4)
            """,
            doc_name, f"{doc_name}_{i}", chunk, embedding.tolist(),
        )
    await db.close()
