from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Journey(Base):
    __tablename__ = "journey"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    progress_id = Column(Integer, ForeignKey("progress.id"))
    progress = relationship("Progress", back_populates="journeys")

    quests = relationship("Quest", back_populates="journeys")

    def __repr__(self):
        return f"<Journey(id={self.id}, title='{self.title}', start_date={self.start_date}, end_date={self.end_date}, progress_id={self.progress_id})>"