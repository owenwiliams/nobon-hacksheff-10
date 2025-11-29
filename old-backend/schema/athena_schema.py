from typing import Optional
from datetime import date
from pydantic import BaseModel

class AthenaBase(BaseModel):
    request: str
    response: str
    date: date

class AthenaCreate(AthenaBase):
    progress_id: int

class AthenaRead(AthenaBase):
    id: int
    progress_id: int

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class AthenaUpdate(BaseModel):
    request: Optional[str] = None
    response: Optional[str] = None
    date: Optional[date] = None
    progress_id: Optional[int] = None