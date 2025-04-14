from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Koneksi PostgreSQL (pakai ENV atau langsung hardcoded dulu)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ml_user:ml_pass@localhost/ml_monitoring")

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base ORM
Base = declarative_base()
