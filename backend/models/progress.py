from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    journeys = relationship("Journey", back_populates="progress")

    entries = relationship("Entry", back_populates="progress")

    athenas = relationship("Athena", back_populates="progress")

    def __repr__(self):
        return f"<Progress(id={self.id}, journey_id={self.journey.id if self.journey else None}, entry_id={self.entry.id if self.entry else None}, athena_id={self.athena.id if self.athena else None})>"