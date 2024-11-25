# project
backend/
├── app.py                  # FastAPI initialization
├── routes/
│   ├── ingestion.py        # Document ingestion API
│   ├── qna.py              # Q&A API
├── services/
│   ├── embeddings.py       # Embedding generation logic
│   ├── database.py         # Database interactions
├── utils/
│   ├── similarity.py       # Similarity calculations
│   ├── cache.py            # Redis caching
├── requirements.txt        # Dependencies
