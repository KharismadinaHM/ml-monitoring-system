from backend.config import engine, Base
from backend.ml_models import metrics  # ⬅️ Penting! Harus diimport agar dikenali

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized!")
