from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    """Add CORS middleware to FastAPI app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Change this in production! TODO
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )