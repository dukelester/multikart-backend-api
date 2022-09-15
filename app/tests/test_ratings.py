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
                           json={ "product_name": " ",
                                "rating": 4,
                                "comment": "testing a rating",
                                "rated_at": "2022-09-15T20:29:51.643Z",
                                })
    assert response.status_code == 422
    assert response.json() == {"detail": [ { "loc": ["body", "product_name" ], 
                                            "msg": "Invalid Product name ", "type": "value_error" 
                                            } ]
                               }
    
def test_creating_rating_wrong_data_validations():
    response = client.post("/ratings/",
                           json={  
                                "product_name": "hello there",
                                "rating": 30,
                                "comment": "product with a lot of nice features",
                                "rated_at": "2022-09-15T20:29:36.908Z"
                                })
    assert response.status_code == 422
    assert type(response.json()) == dict
    assert response.json() == {"detail": [{ "loc": [ "body", "rating" ], 
                                          "msg": "This is an invalid rating", "type": "value_error" 
                                          }]
                             }


