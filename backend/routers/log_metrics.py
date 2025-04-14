from fastapi import APIRouter

router = APIRouter()

@router.post("/log_metrics")  # ✅ Make sure this matches exactly!
def log_metrics():
    return {"message": "Metrics logged successfully"}
