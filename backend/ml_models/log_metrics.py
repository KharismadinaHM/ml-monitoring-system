from sqlalchemy import Column, String, DateTime
from backend.config import Base
import datetime

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    model_name = Column(String, primary_key=True)
    version = Column(String, primary_key=True)
    input_data = Column(String)
    prediction = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, primary_key=True)
