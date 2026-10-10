from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_invoke():
    r=client.post("/agent/invoke",json={"topic":"status"})
    assert r.status_code==200
    assert r.json()["answer"]=="The internal service is operational."
def test_invalid_payload():
    assert client.post("/agent/invoke",json={"topic":"x"}).status_code==422
