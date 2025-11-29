from typing import List, Optional
from pydantic import BaseModel
from backend.schemas.journey import JourneyRead
from backend.schemas.entry import EntryRead
from backend.schemas.athena import AthenaRead

class ProgressCreate(BaseModel):
    journeys: Optional[List[int]] = []
    entries: Optional[List[int]] = []
    athenas: Optional[List[int]] = []

class ProgressRead(BaseModel):
    id: int
    journeys: List[JourneyRead] = []
    entries: List[EntryRead] = []
    athenas: List[AthenaRead] = []

    class Config:
        orm_mode = True

class ProgressUpdate(BaseModel):
    journeys: Optional[List[int]] = None
    entries: Optional[List[int]] = Nonej
    athenas: Optional[List[int]] = None