from sqlalchemy import Column, String, Float, DateTime
from backend.config import Base
import datetime

class ModelMetrics(Base):
    __tablename__ = "model_metrics"

    model_name = Column(String, primary_key=True)
    version = Column(String, primary_key=True)
    accuracy = Column(Float, nullable=False)
    precision = Column(Float, nullable=False)
    recall = Column(Float, nullable=False)
    f1_score = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
