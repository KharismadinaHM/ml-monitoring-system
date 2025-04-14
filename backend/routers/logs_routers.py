from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.ml_models.logs import PredictionLog
from pydantic import BaseModel
from typing import List, Optional
import datetime

router = APIRouter()

class LogIn(BaseModel):
    model_name: str
    version: str
    input_data: str
    prediction: str
    actual: Optional[str] = None
    timestamp: Optional[datetime.datetime] = None

class LogOut(LogIn):
    id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/logs")
def add_log(log: LogIn, db: Session = Depends(get_db)):
    log_entry = PredictionLog(**log.dict())
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return {"message": "✅ Log saved", "log_id": log_entry.id}

@router.get("/logs", response_model=List[LogOut])
def get_logs(db: Session = Depends(get_db)):
    return db.query(PredictionLog).all()
