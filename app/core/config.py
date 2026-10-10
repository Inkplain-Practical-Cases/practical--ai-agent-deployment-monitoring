import os
from pydantic import BaseModel,Field
class RuntimeConfig(BaseModel):
    service_name:str=Field(min_length=3)
    environment:str=Field(pattern="^(local|test|production)$")
def service_load_config()->RuntimeConfig:
    return RuntimeConfig(service_name=os.getenv("SERVICE_NAME","northstar-agent"),environment=os.getenv("APP_ENV","local"))
