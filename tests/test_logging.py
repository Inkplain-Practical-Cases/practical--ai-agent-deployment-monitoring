import json,logging
from app.core.logging import service_log_event
def test_safe_logs(caplog):
    with caplog.at_level(logging.INFO,logger="agent.operations"): service_log_event("agent_invocation","success")
    assert json.loads(caplog.records[-1].message)=={"event":"agent_invocation","result":"success"}
