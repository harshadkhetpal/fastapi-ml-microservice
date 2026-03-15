# Author: Harshad Khetpal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Harshad ML Service", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
Instrumentator().instrument(app).expose(app)

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}
