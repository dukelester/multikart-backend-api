from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_index():
    response = client.get("/polls")
    assert response.status_code == 200