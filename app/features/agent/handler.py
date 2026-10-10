from app.features.agent.service import service_answer
def handle_request(topic:str)->dict:
    return service_answer(topic)
