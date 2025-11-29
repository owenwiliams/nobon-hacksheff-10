from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.db import Base

class Journey(Base):
    __tablename__ = "journey"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    quests = relationship("Quest", back_populates="journeys")

class Quest(Base):
    __tablename__ = "quest"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    start_date = Column(Date, index=True)
    due_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    tasks = relationship("Task", back_populates="quests")

    journey_id = Column(Integer, ForeignKey("journey.id"))
    journey = relationship("Journey", back_populates="quests")

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    body = Column(String, index=True)
    is_completed = Column(Boolean, index=True)

    quest_id = Column(Integer, ForeignKey("quest.id"))
    quest = relationship("Quest", back_populates="tasks")

class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    entry_date = Column(Date, index=True)