from fastapi import FastAPI
from backend.database import engine, Base
from backend.database.models import Athena, Entry, Journey, Progress, Quest

# Remove once database is finalised
Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}