from fastapi import FastAPI
from routes import ingestion, qna

app = FastAPI()

# Include routes
app.include_router(ingestion.router, prefix="/ingest")
app.include_router(qna.router, prefix="/qna")
