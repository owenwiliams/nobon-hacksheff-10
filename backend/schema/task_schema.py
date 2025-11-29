from typing import Optional
from pydantic import BaseModel

class QuestBase(BaseModel):
    body: str
    is_completed: bool

class QuestCreate(QuestBase):
    quest_id: int

class QuestRead(QuestBase):
    id: int
    quest_id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class QuestUpdate(BaseModel):
    body: Optional[str] = None
    is_completed: Optional[bool] = None
    quest_id: Optional[int] = None