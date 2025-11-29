from typing import Optional
from datetime import date
from pydantic import BaseModel

class EntryBase(BaseModel):
    title: str
    body: str
    entry_date: date

class EntryCreate(EntryBase):
    progress_id: int

class EntryRead(EntryBase):
    id: int
    progress_id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class EntryUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    entry_date: Optional[date] = None
    progress_id: Optional[int] = None