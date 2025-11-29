from typing import Optional
from datetime import date
from pydantic import BaseModel

class QuestBase(BaseModel):
    title: str
    start_date: date
    due_date: date
    end_date: date

class QuestCreate(QuestBase):
    journey_id: int

class QuestRead(QuestBase):
    id: int
    journey_id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class QuestUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    end_date: Optional[date] = None
    journey_id: Optional[int] = None