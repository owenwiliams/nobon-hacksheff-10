from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    entry_date = Column(Date, index=True)

    progress_id = Column(Integer, ForeignKey("progress.id"))
    progress = relationship("Progress", back_populates="entry")