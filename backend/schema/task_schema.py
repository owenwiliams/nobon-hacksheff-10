from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    body: str
    is_completed: bool

class TaskCreate(TaskBase):
    quest_id: int

class TaskRead(TaskBase):
    id: int
    quest_id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class TaskUpdate(BaseModel):
    body: Optional[str] = None
    is_completed: Optional[bool] = None
    quest_id: Optional[int] = None