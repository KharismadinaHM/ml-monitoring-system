from sqlalchemy.orm import Session
from backend.ml_models.metrics import ModelMetrics
import datetime

def log_model_metrics(
    db: Session,
    model_name: str,
    version: str,
    accuracy: float,
    precision: float,
    recall: float,
    f1_score: float
):
    # Buat objek metrics
    metrics = ModelMetrics(
        model_name=model_name,
        version=version,
        accuracy=accuracy,
        precision=precision,
        recall=recall,
        f1_score=f1_score,
        timestamp=datetime.datetime.utcnow()
    )

    # Cek apakah sudah ada entry yang sama
    existing = db.query(ModelMetrics).filter_by(model_name=model_name, version=version).first()
    if existing:
        db.delete(existing)

    # Tambahkan dan commit
    db.add(metrics)
    db.commit()
    print(f"✅ Metrics saved for {model_name} v{version}")
