from fastapi import APIRouter
from pydantic import BaseModel,Field
from app.features.agent.handler import handle_request
router=APIRouter(prefix="/agent",tags=["Agent"])
class Request(BaseModel):
    topic:str=Field(min_length=3,max_length=100)
@router.post("/invoke")
def invoke(payload:Request)->dict: return handle_request(payload.topic)
