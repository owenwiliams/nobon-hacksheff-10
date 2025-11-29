from fastapi import FastAPI
from backend.routes import entry_routes as entry_router

app = FastAPI()
app.include_router(entry_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}