from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from backend.config import SessionLocal
from backend.ml_models.logs import PredictionLog  # Pastikan path ini sesuai

router = APIRouter()

# Request body schema
class LogIn(BaseModel):
    model_name: str
    version: str
    input_data: str
    prediction: str
    actual: Optional[str] = None
    timestamp: Optional[datetime] = None

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/logs")
def add_prediction_log(log: LogIn, db: Session = Depends(get_db)):
    log_entry = PredictionLog(**log.dict())
    db.add(log_entry)
    db.commit()
    return {"message": "✅ Prediction log saved"}
