import pytest
from fastapi.testclient import TestClient
from app import app
from services.database import db_service

@pytest.fixture(scope="module")
def test_client():
    """
    Provide a TestClient instance for API tests.
    """
    return TestClient(app)

@pytest.fixture(scope="module", autouse=True)
async def setup_test_database():
    """
    Create and populate a test database before running tests.
    Cleanup after all tests are done.
    """
    await db_service.connect()
    await db_service.execute("TRUNCATE document_embeddings, documents RESTART IDENTITY;")
    yield
    await db_service.execute("TRUNCATE document_embeddings, documents RESTART IDENTITY;")
