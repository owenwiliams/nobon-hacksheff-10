from fastapi import FastAPI
from routes.entry_routes import router as entry_router
from routes.quest_routes import router as quest_router
from routes.task_routes import router as task_router
from db import Base, engine
import models  # Import models so SQLAlchemy knows about them

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(entry_router)
app.include_router(quest_router)
app.include_router(task_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}