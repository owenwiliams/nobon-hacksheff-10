from typing import Optional
from datetime import date
from pydantic import BaseModel

class JourneyBase(BaseModel):
    title: str
    start_date: date
    end_date: date

class JourneyCreate(JourneyBase):
    pass

class JourneyRead(JourneyBase):
    id: int

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be returned as Pydantic objects

class JourneyUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
