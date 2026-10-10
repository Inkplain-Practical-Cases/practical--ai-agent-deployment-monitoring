from pathlib import Path
def test_container_contract():
    root=Path(__file__).resolve().parents[1]
    docker=(root/"Dockerfile").read_text()
    assert "USER 65532:65532" in docker
    assert "uvicorn" in docker
    assert "healthcheck:" in (root/"docker-compose.yml").read_text()
