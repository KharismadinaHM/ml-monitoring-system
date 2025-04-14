from fastapi import FastAPI
from backend.routers import log_metrics
from backend.api import metrics
from backend.api import log_metrics
from backend.routers import prediction_logs
from backend.routers import logs
from backend.routers import logs_router





app = FastAPI()

# Routes
app.include_router(log_metrics.router)
app.include_router(metrics.router, prefix="/api")
app.include_router(log_metrics.router, prefix="/api")
app.include_router(prediction_logs.router)
app.include_router(logs.router)
app.include_router(logs_router.router)





@app.get("/")
def root():
    return {"message": "Welcome to the ML Monitoring API 👋"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "running"}

# Jalankan server dengan uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


