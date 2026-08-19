from fastapi import FastAPI
from app.routers.auth import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def home():
    return {"message": "Authentication API"}