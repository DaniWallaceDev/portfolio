from fastapi import FastAPI
from src.routers import api_router
import uvicorn

app = FastAPI(
    title="fastAPI Final Project"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)