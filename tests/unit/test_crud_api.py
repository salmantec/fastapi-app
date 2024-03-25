from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test healthcheck API:
def test_main_route():
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}