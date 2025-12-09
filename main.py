from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from routers.edges import router as edges_router

app = FastAPI(
    title="Real-Time Image Transform API",
    description="Upload an image → get Sobel, Canny, Laplacian, Scharr, Histogram, HOG transforms.",
    version="1.0.0"
)

# Serve frontend folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

# Include router
app.include_router(edges_router)

@app.get("/api")
def home():
    return {"message": "Image Transform API is running!"}
