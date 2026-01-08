from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.routes.generate import router as generate_router

app = FastAPI(title="Architecta", version="0.1.0")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(generate_router)

# Serve frontend static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Optional health check
@app.get("/health")
def health():
    return {"status": "ok"}
