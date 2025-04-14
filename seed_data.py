from backend.config import SessionLocal
from backend.ml_models.metrics import ModelMetrics
import datetime

# Buat koneksi ke DB
db = SessionLocal()

# Data dummy
metrics_data = [
    ModelMetrics(
        model_name="model-a",
        version="1.0",
        accuracy=0.91,
        precision=0.89,
        recall=0.88,
        f1_score=0.885,
        timestamp=datetime.datetime.utcnow()
    ),
    ModelMetrics(
        model_name="model-b",
        version="2.0",
        accuracy=0.94,
        precision=0.92,
        recall=0.90,
        f1_score=0.91,
        timestamp=datetime.datetime.utcnow()
    ),
]

# Insert ke DB
db.add_all(metrics_data)
db.commit()
db.close()

print("✅ Seed data berhasil dimasukkan!")
