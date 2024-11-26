import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_qna_success():
    # Mock query to the Q&A API
    response = client.get("/api/qna", params={"query": "What is this about?"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "context" in response.json()

def test_qna_no_results():
    # Mock query that has no matching embeddings
    response = client.get("/api/qna", params={"query": "Unrelated query"})
    assert response.status_code == 200
    assert response.json()["answer"] == ""  # No answer generated
    assert response.json()["context"] == []  # No relevant context found

def test_qna_invalid_request():
    # Test invalid request parameters
    response = client.get("/api/qna")
    assert response.status_code == 422  # Missing required parameter
