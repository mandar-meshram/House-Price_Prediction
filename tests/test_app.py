from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/predict", json={
        'location' : "delhi",
        'area' : 1200,
        'bedrooms' : 3,
        'bathrooms' : 2,
        'furnishing' : "furnished"
    })

    assert response.status_code == 200
    assert 'price' in response.json()