# AI Agent Deployment & Monitoring

Forward Deployed Engineering Starter, six cumulative branches. A Python FastAPI service with explicit offline provider, validated configuration, metadata-only structured events, liveness/readiness, a non-root Dockerfile, Compose and test suites.

```bash
pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

Docker: `docker compose up --build`. Endpoints POST /agent/invoke with {"topic":"status"}, GET /health, GET /ready. No paid LLM or cloud credentials. These are simulated internal agent operations; a production rollout needs secrets management, authentication, metrics and remote orchestration.

Branches: step-01-build-the-agent-service-api, step-02-validate-runtime-configuration, step-03-record-safe-structured-events, step-04-add-health-and-readiness-probes, step-05-containerize-and-configure-delivery, step-06-harden-and-verify-deployment. Each has STEP-N.crd, STEP-N.md and tests. Main has FINAL.crd and seven-job Github Actions.
