from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    body: str
    complete: bool = False

class TaskCreate(TaskBase):
    quest_id: int 

class TaskRead(TaskBase):
    id: int
    body: str
    complete: bool
    quest_id: int

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    body: Optional[str] = None
    complete: Optional[bool] = None
    quest_id: Optional[int] = None
    