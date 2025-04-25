import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import cv

# Create FastAPI app
app = FastAPI(
    title="CV RAG API",
    description="API for CV upload and search using RAG (Retrieval-Augmented Generation)",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(cv.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to CV RAG API. Visit /docs for API documentation."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
