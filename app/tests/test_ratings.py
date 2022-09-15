from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_all_ratings():
    response = client.get("/ratings")
    assert response.status_code == 200
    assert type(response.json()) == list
    
def test_creating_rating():
    response = client.post("/ratings/", 
                           json={  
                                "product_name": "testing product",
                                "rating": 4,
                                "comment": "testing a rating",
                                "rated_at": "2022-09-15T20:29:51.643Z",
                                })
    assert response.status_code == 201
    assert "testing product" in list(response.json().values())
    assert "id" in list(response.json().keys())
    
def test_creating_rating_wrong_data():
    response = client.post("/ratings/",
                           json={  
                                "rating": 4,
                                "comment": "testing a rating",
                                "rated_at": "2022-09-15T20:29:51.643Z",
                                })
    assert response.status_code == 422
