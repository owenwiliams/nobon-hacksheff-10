from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel
from backend.schemas.task import TaskBase

class QuestBase(BaseModel):
    title: str
    date_created: datetime
    date_completed: Optional[datetime] = None
    due_date: Optional[date] = None

class QuestCreate(QuestBase):
    journey_id: int
    tasks: Optional[List[TaskBase]] = []  

class QuestRead(QuestBase):
    id: int
    title: str
    date_created: datetime
    date_completed: Optional[datetime] = None
    due_date: Optional[date] = None
    tasks: List[TaskBase] = []

    class Config:
        orm_mode = True

class QuestUpdate(BaseModel):
    title: Optional[str] = None
    date_completed: Optional[datetime] = None
    due_date: Optional[date] = None
    journey_id: Optional[int] = None
    tasks: Optional[List[int]] = None