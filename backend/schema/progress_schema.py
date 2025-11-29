from typing import List, Optional
from pydantic import BaseModel
from backend.schemas.journey import JourneyBase

class ProgressBase(BaseModel):
    name: str

class ProgressCreate(ProgressBase):
    journeys: Optional[List[JourneyBase]] = []

class ProgressRead(ProgressBase):
    id: int
    journeys: List[JourneyBase] = []

    class Config:
        orm_mode = True