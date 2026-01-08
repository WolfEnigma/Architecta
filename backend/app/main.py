from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes.generate import router as generate_router

app = FastAPI(
    title="Architecta",
    version="0.1.0"
)

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # <-- in production, restrict to trusted origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_router)


@app.get("/health")
def health():
    return {"status": "ok"}
