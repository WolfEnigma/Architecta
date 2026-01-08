from fastapi import FastAPI
from backend.app.routes.generate import router as generate_router

app = FastAPI(
    title="Architecta",
    version="0.1.0"
)

app.include_router(generate_router)


@app.get("/health")
def health():
    return {"status": "ok"}
