from typing import List, Optional
from sqlalchemy.orm import Session
from backend import models, schema

def create_journey(db: Session, journey_in: schema.JourneyCreate) -> models.Journey:
    db_journey = models.Journey(**journey_in.dict())
    db.add(db_journey)
    db.commit()
    db.refresh(db_journey)
    return db_journey

def get_journey(db: Session, journey_id: int) -> Optional[models.Journey]:
    return db.query(models.Journey).filter(models.Journey.id == journey_id).first()

def get_journeys(db: Session, skip: int = 0, limit: int = 100) -> List[models.Journey]:
    return db.query(models.Journey).offset(skip).limit(limit).all()

def update_journey(db: Session, journey_id: int, journey_in: schema.JourneyUpdate) -> Optional[models.Journey]:
    db_journey = db.query(models.Journey).filter(models.Journey.id == journey_id).first()
    if db_journey is None:
        return None
    update_data = journey_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_journey, key, value)
    db.add(db_journey)
    db.commit()
    db.refresh(db_journey)
    return db_journey

def delete_journey(db: Session, journey_id: int) -> Optional[models.Journey]:
    db_journey = db.query(models.Journey).filter(models.Journey.id == journey_id).first()
    if db_journey is None:
        return None
    db.delete(db_journey)
    db.commit()
    return db_journey