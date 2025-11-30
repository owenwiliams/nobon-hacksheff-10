from fastapi import FastAPI
from routes.entry_routes import router as entry_router
from routes.quest_routes import router as quest_router
from routes.task_routes import router as task_router
from routes.journey_routes import router as journey_router
from routes.gemini_routes import router as gemini_router
from db import Base, engine
from fastapi.middleware.cors import CORSMiddleware

import models  # Import models so SQLAlchemy knows about them

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entry_router)
app.include_router(quest_router)
app.include_router(task_router)
app.include_router(journey_router)
app.include_router(gemini_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}