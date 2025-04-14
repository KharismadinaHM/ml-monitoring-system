from sqlalchemy import Column, Integer, String, DateTime
from backend.config import Base
import datetime

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    input_data = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    actual = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
