"""Validate persisted deployment HTTP request and event foreign-key relationship."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_deployment_api_audit(tmp_path):
    path=str(tmp_path/"deployment.sqlite3")
    rid=provider_record_request_audit("GET","/health",200,1.2,path)
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM deployment_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("SELECT COUNT(*) FROM deployment_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("PRAGMA foreign_key_check").fetchall()==[]
