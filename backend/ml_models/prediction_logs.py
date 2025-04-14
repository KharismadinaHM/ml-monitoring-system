from sqlalchemy import Column, String, Float, DateTime, Integer
from backend.config import Base
import datetime

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    input_data = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    true_label = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
