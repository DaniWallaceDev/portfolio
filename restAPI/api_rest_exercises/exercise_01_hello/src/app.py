import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def root():
    return {"message": "Hello Dani"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/query_params/")
async def query(name: str = str, surname: str = str):
    return {"message": f"Hello {name} {surname}, good morning"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)