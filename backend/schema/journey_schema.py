from typing import Optional
from datetime import date
from pydantic import BaseModel

class JourneyBase(BaseModel):
    title: str
    start_date: date
    end_date: date

