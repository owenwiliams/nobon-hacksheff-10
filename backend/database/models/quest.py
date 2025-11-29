from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    objective = Column(String, index=True)
    complete = Column(Integer, index=True)
    date_created = Column(Date, index=True)
    date_completed = Column(Date, index=True)
    due_date = Column(Date, index=True)

    journey_id = Column(Integer, ForeignKey("journey.id"))
    journey = relationship("Journey", back_populates="quests")