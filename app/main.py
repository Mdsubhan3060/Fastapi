from fastapi import FastAPI
from app.routers.auth import router
from app.routers.admin import router as admin_router

app = FastAPI()

app.include_router(router)

app.include_router(admin_router)

@app.get("/")
async def home():
    return {"message": "Authentication API"}