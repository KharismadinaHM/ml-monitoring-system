from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.ml_models.metrics import ModelMetrics
from pydantic import BaseModel
from typing import List, Optional
import datetime

router = APIRouter()

# ✅ Schema input/output
class MetricsIn(BaseModel):
    model_name: str
    version: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    timestamp: Optional[datetime.datetime] = None

class MetricsOut(MetricsIn):
    class Config:
        orm_mode = True  # ✅ Ini penting agar bisa return SQLAlchemy object

# ✅ Dependency database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ POST route
@router.post("/metrics")
def add_metrics(metrics: MetricsIn, db: Session = Depends(get_db)):
    metric_entry = ModelMetrics(**metrics.dict())
    db.add(metric_entry)
    db.commit()
    return {"message": "✅ Metrics saved"}

# ✅ GET route
@router.get("/metrics", response_model=List[MetricsOut])
def get_metrics(db: Session = Depends(get_db)):
    return db.query(ModelMetrics).all()
