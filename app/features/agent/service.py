from app.providers.response_provider import provider_response
def service_answer(topic:str)->dict:
    return {"answer":provider_response(topic),"topic":topic}
