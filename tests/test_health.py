from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health_and_ready():
    assert client.get("/health").json()["status"]=="ok"
    assert client.get("/ready").json()["ready"] is True
