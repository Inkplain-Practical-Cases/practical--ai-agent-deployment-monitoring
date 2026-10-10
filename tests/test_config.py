import pytest
from pydantic import ValidationError
from app.core.config import RuntimeConfig,service_load_config
def test_defaults():
    assert service_load_config().environment=="local"
def test_rejects_invalid_runtime():
    with pytest.raises(ValidationError): RuntimeConfig(service_name="x",environment="unknown")
