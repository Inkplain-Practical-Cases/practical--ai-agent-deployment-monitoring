def provider_response(topic:str)->str:
    replies={"status":"The internal service is operational.","support":"Contact the operations support queue.","deployment":"Deploy through a tested CI pipeline."}
    return replies.get(topic.lower(),"No approved answer is available for this topic.")
