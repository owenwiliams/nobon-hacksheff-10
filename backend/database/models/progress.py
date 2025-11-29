from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    journey = relationship("Journey", back_populates="progress")

    entry = relationship("Entry", back_populates="progress")

    athena = relationship("Athena", back_populates="progress")