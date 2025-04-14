from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.ml_models.log_metrics import PredictionLog
from pydantic import BaseModel
from typing import List
import datetime

router = APIRouter()

class LogIn(BaseModel):
    model_name: str
    version: str
    input_data: str
    prediction: str
    timestamp: datetime.datetime = datetime.datetime.utcnow()

class LogOut(LogIn):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log")
def log_prediction(log: LogIn, db: Session = next(get_db())):
    log_entry = PredictionLog(**log.dict())
    db.add(log_entry)
    db.commit()
    return {"message": "✅ Prediction log saved"}

@router.get("/log", response_model=List[LogOut])
def get_logs(db: Session = next(get_db())):
    return db.query(PredictionLog).all()
