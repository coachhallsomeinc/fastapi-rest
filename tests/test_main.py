# tests using pytest
from fastapi.testclient import TestClient

from main import app
from routers import todos

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"