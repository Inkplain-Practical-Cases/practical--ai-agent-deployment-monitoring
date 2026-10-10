from fastapi.testclient import TestClient
from app.main import app
def test_too_large_payload_rejected():
    r=TestClient(app).post("/agent/invoke",json={"topic":"x"*101})
    assert r.status_code==422
