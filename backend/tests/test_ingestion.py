import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ingest_document_success():
    # Simulate uploading a valid text file
    response = client.post(
        "/api/ingestion/",
        files={"file": ("test_document.txt", b"This is a test document.")}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Document ingested successfully"
    assert "chunks" in response.json()

def test_ingest_document_invalid_format():
    # Simulate uploading a file in an invalid format
    response = client.post(
        "/api/ingestion/",
        files={"file": ("test_document.pdf", b"%PDF-1.4 Invalid content.")}
    )
    assert response.status_code == 422  # Unprocessable Entity

def test_ingest_document_empty_file():
    # Simulate uploading an empty file
    response = client.post(
        "/api/ingestion/",
        files={"file": ("empty.txt", b"")}
    )
    assert response.status_code == 422
    assert "error" in response.json()
