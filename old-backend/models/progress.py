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
        return f"<Progress(id={self.id})>"