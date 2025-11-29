from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    body = Column(String, index=True)
    complete = Column(Boolean, index=True)

    quest_id = Column(Integer, ForeignKey("quests.id"))
    quest = relationship("Quest", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, body='{self.body}', complete='{self.complete}', quest_id={self.quest_id})>"