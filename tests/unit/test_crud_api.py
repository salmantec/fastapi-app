import os
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "sqlite:////tmp/test.db"

from app.main import app  # noqa: E402

client = TestClient(app)


# Test healthcheck API:
def test_main_route():
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}
