from app.core.config import service_load_config
def service_health()->dict:
    return {"status":"ok"}
def service_readiness()->dict:
    conf=service_load_config()
    return {"ready":bool(conf.service_name)}
