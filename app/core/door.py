from fastapi import APIRouter
from app.core.health import service_health,service_readiness
router=APIRouter(tags=["Operations"])
@router.get("/health")
def health()->dict: return service_health()
@router.get("/ready")
def ready()->dict: return service_readiness()
