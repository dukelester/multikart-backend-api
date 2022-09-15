from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "description" : " Welcome to the Multikart Backend Api" }