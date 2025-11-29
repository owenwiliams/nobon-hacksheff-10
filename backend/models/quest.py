from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(Date, index=True)
    date_completed = Column(Date, index=True)
    due_date = Column(Date, index=True)

    tasks = relationship("Task", back_populates="quest")

    journey_id = Column(Integer, ForeignKey("journey.id"))
    journey = relationship("Journey", back_populates="quests")

    def __repr__(self):
        return f"<Quest(id={self.id}, date_created={self.date_created}, date_completed={self.date_completed}, due_date={self.due_date}, journey_id={self.journey_id})>"