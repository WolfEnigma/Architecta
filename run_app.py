import webbrowser
import uvicorn

# Open the frontend in default browser
webbrowser.open("frontend/index.html")

# Start FastAPI backend
uvicorn.run(
    "backend.app.main:app",
    host="127.0.0.1",
    port=8000,
    reload=False
)
