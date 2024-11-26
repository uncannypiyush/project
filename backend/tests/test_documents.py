import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_toggle_document_success():
    # Mock toggling a document's active status
    response = client.patch("/api/documents/1/toggle")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "document_id" in response.json()
    assert "new_status" in response.json()

def test_toggle_document_not_found():
    # Test toggling a non-existent document
    response = client.patch("/api/documents/9999/toggle")
    assert response.status_code == 404
    assert "error" in response.json()
