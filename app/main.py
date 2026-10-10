from fastapi import FastAPI
from app.core.config import service_load_config
from app.core.door import router as ops_router
from app.features.agent.door import router as agent_router
settings=service_load_config()
app=FastAPI(title=settings.service_name)
app.include_router(agent_router)
app.include_router(ops_router)
