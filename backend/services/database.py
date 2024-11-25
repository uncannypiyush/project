import asyncpg
from typing import List, Tuple

# Database configuration
DB_URL = "postgresql://user:password@localhost/dbname"

# Initialize connection pool
async def init_db_pool():
    return await asyncpg.create_pool(DB_URL)

# Helper function to execute queries
async def execute_query(query: str, *args):
    pool = await init_db_pool()
    async with pool.acquire() as conn:
        try:
            result = await conn.execute(query, *args)
            return result
        finally:
            await pool.close()

# Store embeddings in the database
async def store_embeddings(document_name: str, chunks: List[str], embeddings: List[List[float]]):
    pool = await init_db_pool()
    async with pool.acquire() as conn:
        try:
            # Start a transaction
            async with conn.transaction():
                for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                    await conn.execute(
                        """
                        INSERT INTO document_embeddings (document_name, chunk_id, content, embedding)
                        VALUES ($1, $2, $3, $4)
                        """,
                        document_name,
                        f"{document_name}_{idx}",
                        chunk,
                        embedding,
                    )
        finally:
            await pool.close()

# Retrieve embeddings for similarity search
async def retrieve_embeddings(document_ids: List[int] = None) -> List[Tuple[str, List[float]]]:
    pool = await init_db_pool()
    async with pool.acquire() as conn:
        try:
            if document_ids:
                query = """
                SELECT content, embedding 
                FROM document_embeddings
                JOIN documents ON documents.name = document_embeddings.document_name
                WHERE documents.id = ANY($1::int[])
                """
                rows = await conn.fetch(query, document_ids)
            else:
                query = """
                SELECT content, embedding 
                FROM document_embeddings
                JOIN documents ON documents.name = document_embeddings.document_name
                WHERE documents.is_active = TRUE
                """
                rows = await conn.fetch(query)

            return [(row['content'], row['embedding']) for row in rows]
        finally:
            await pool.close()

# Toggle document status
async def toggle_document_status(document_id: int):
    pool = await init_db_pool()
    async with pool.acquire() as conn:
        try:
            # Check current status
            current_status = await conn.fetchval(
                "SELECT is_active FROM documents WHERE id = $1", document_id
            )
            if current_status is None:
                raise ValueError("Document not found")

            # Toggle status
            new_status = not current_status
            await conn.execute(
                "UPDATE documents SET is_active = $1 WHERE id = $2", new_status, document_id
            )
            return new_status
        finally:
            await pool.close()
