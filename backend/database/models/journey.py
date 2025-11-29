from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Journey(Base):
    __tablename__ = "journey"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    progress_id = Column(Integer, ForeignKey("progress.id"))
    progress = relationship("Progress", back_populates="journeys")

    quests = relationship("Quest", back_populates="journey")