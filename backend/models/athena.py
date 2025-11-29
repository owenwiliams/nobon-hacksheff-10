from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Athena(Base):
    __tablename__ = "athena"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    request = Column(String, index=True)
    response = Column(String, index=True)
    date = Column(Date, index=True)

    progress_id = Column(Integer, ForeignKey("progress.id"))
    progress = relationship("Progress", back_populates="athena")

    def __repr__(self):
        return f"<Athena(id={self.id}, request='{self.request}', response='{self.response}', date={self.date}, progress_id={self.progress_id})>"