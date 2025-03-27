from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "running"}

# Jalankan server dengan uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
