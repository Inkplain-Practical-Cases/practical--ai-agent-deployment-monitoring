from fastapi import FastAPI
from app.features.agent.door import router
app=FastAPI(title="AI Agent Deployment and Monitoring")
app.include_router(router)
