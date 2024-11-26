backend/
├── app.py                  # Entry point for the FastAPI app
├── config/                 # Configuration files
│   ├── settings.py         # App configuration and environment variables
│   ├── logger.py           # Logging configuration
├── routes/                 # API routes
│   ├── ingestion.py        # Endpoints for document ingestion
│   ├── qna.py              # Endpoints for Q&A features
│   ├── documents.py        # Endpoints for document metadata management
├── services/               # Core business logic
│   ├── embeddings.py       # Embedding generation and storage logic
│   ├── database.py         # Database interaction logic
│   ├── qna_service.py      # Q&A retrieval and generation logic
│   ├── cache.py            # Redis caching logic
├── models/                 # Database models and schemas
│   ├── db_models.py        # ORM models for database tables
│   ├── request_schemas.py  # Pydantic schemas for request validation
│   ├── response_schemas.py # Pydantic schemas for response validation
├── utils/                  # Utility functions and helpers
│   ├── similarity.py       # Functions for similarity calculations
│   ├── test_data.py        # Functions to generate large test data
├── tests/                  # Test cases
│   ├── test_ingestion.py   # Unit tests for ingestion API
│   ├── test_qna.py         # Unit tests for Q&A API
│   ├── test_documents.py   # Unit tests for document management
├── requirements.txt        # Project dependencies
├── Dockerfile              # Dockerfile for containerizing the application
├── deploy.yaml             # Compose file for CI/CD setup
├── kube.yaml               # Compose file for multi-container setup
├── README.md               # Project documentation
