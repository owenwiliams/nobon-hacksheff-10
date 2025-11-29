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
        orm_mode = True