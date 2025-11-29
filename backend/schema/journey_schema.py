from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel
from backend.schemas.quest import QuestBase

class JourneyBase(BaseModel):
    title: str
    start_date: date
    end_date: Optional[datetime] = None

class JourneyCreate(JourneyBase):
    progress_id: int
    quests: Optional[List[QuestBase]] = []

class JourneyRead(JourneyBase):
    id: int
    title: str
    start_date: date
    end_date: Optional[datetime] = None
    progress_id: int
    quests: List[QuestBase] = []

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class JourneyUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    progress_id: Optional[int] = None
    quests: Optional[List[int]] = None