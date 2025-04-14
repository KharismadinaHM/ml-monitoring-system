from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.ml_models.logging import log_model_metrics

db: Session = SessionLocal()

log_model_metrics(
    db=db,
    model_name="churn-predictor",
    version="1.0",
    accuracy=0.91,
    precision=0.88,
    recall=0.85,
    f1_score=0.86
)
