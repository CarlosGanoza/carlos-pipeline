from fastapi import FastAPI
from src.generated.module_001 import build_payload_001

app = FastAPI(title="Large Demo Python API")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/sample")
def sample() -> dict[str, object]:
    return build_payload_001(3)
