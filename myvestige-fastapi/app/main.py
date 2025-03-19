from fastapi import FastAPI

from app.admin.admin import setup_admin, init_admin
from app.middleware.cors import add_cors_middleware
from app.middleware.logging import LoggingMiddleware

from app.api.users.routes import router as users_router
from app.api.pages.routes import router as pages_router
app = FastAPI()

# Add CORS
add_cors_middleware(app)

# Add logging middleware
app.add_middleware(LoggingMiddleware)

@app.on_event("startup")
async def startup():
    await init_admin()

app.mount("/admin", app.admin.app)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(pages_router, prefix="/pages", tags=["Pages"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/test")
async def test():
    return {"message": "test"}
