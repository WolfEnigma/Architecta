from fastapi import FastAPI

app = FastAPI(
    title="Architecta",
    description="Professional Project Architecture & Scaffolding Engine",
    version="0.1.0"
)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "service": "architecta"}
