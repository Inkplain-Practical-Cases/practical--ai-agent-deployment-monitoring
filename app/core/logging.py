import json,logging
logger=logging.getLogger("agent.operations")
def service_log_event(event:str,result:str)->None:
    # Never log user payloads, passwords, tokens or raw prompts.
    logger.info(json.dumps({"event":event,"result":result},sort_keys=True))
