from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.ml_models.prediction_logs import PredictionLog
from pydantic import BaseModel
from typing import Optional
import datetime

router = APIRouter()

class PredictionIn(BaseModel):
    model_name: str
    version: str
    input_data: str
    prediction: str
    true_label: Optional[str] = None
    timestamp: Optional[datetime.datetime] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/prediction_logs")
def log_prediction(data: PredictionIn, db: Session = Depends(get_db)):
    log_entry = PredictionLog(**data.dict())
    db.add(log_entry)
    db.commit()
    return {"message": "✅ Prediction log saved"}
