import webbrowser
import threading
import uvicorn

def start_server():
    uvicorn.run(
        "backend.app.main:app",  # backend path
        host="127.0.0.1",
        port=8000,
        reload=False
    )

if __name__ == "__main__":
    # Start backend server in a separate thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Open frontend in default browser
    webbrowser.open("http://127.0.0.1:8000")

    # Keep the main thread alive while backend is running
    server_thread.join()
