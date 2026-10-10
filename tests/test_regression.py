from fastapi.testclient import TestClient
from app.main import app
def test_operations_and_agent():
    client=TestClient(app)
    for endpoint in ("/health","/ready"):
        assert client.get(endpoint).status_code==200
    for topic in ("support","deployment","not-configured"):
        r=client.post("/agent/invoke",json={"topic":topic})
        assert r.status_code==200
        assert r.json()["answer"]
