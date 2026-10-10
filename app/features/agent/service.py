from app.providers.response_provider import provider_response
from app.core.logging import service_log_event
def service_answer(topic:str)->dict:
    result={"answer":provider_response(topic),"topic":topic}
    service_log_event("agent_invocation","success")
    return result
