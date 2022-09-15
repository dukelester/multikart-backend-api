from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)
def test_all_products_route():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == { " all": "Products " }