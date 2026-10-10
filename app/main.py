from fastapi import FastAPI
from app.core.config import service_load_config
from app.features.agent.door import router
settings=service_load_config()
app=FastAPI(title=settings.service_name)
app.include_router(router)
