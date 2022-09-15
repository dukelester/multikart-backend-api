from urllib import response
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_all_products_route():
    response = client.get("/products")
    assert response.status_code == 200
    assert type(response.json()) == list
    
def test_creating_new_product_no_body():
    response = client.post("/products/")
    assert response.status_code == 422

def test_creating_product_with_bad_data():
    response = client.post("/products/", json=
       {
        "product_id": "3fa85f64-5717-4562-b3fc-2c963f66afa4",
        "product_title": "string",
        "description": "string",
        "category": "string",
        "price": 0,
        "quantity_in_stock": 0,
        "created_at": "2022-09-15T15:50:32.626Z",
        "isActive": True
        
    })
    assert response.status_code == 422
    
def test_creating_product_with_good_data():
    response = client.post("/products/", json=
       {
        "product_id": "3fa85f64-5717-4562-b3fc-9c963f66afa2",
        "product_title": "testing product",
        "description": "testing a product to be storted in db",
        "category": "tests",
        "price": 3400,
        "quantity_in_stock": 34,
        "created_at": "2022-09-15T15:50:32.626Z",
        "isActive": True
        
    })
    assert response.status_code == 201