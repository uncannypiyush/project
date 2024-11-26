import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ingest_document():
    response = client.post("/api/ingestion", files={"file": ("test.txt", b"Sample document content.")})
    assert response.status_code == 200
    assert "Document ingested successfully" in response.json()["message"]
