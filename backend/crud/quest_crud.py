from typing import List, Optional
from sqlalchemy.orm import Session
from models import Quest
from schema import quest_schema as schema

def create_quest(db: Session, quest_in: QuestCreate) -> Quest:
    db_quest = Quest(**quest_in.model_dump())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def get_quest(db: Session, quest_id: int) -> Optional[Quest]:
    return db.query(Quest).filter(Quest.id == quest_id).first()

def get_all_quests(db: Session, skip: int = 0, limit: int = 100) -> List[Quest]:
    return db.query(Quest).offset(skip).limit(limit).all()

<<<<<<< HEAD
def get_quests_by_journey(db: Session, journey_id: int) -> List[Quest]:
    return db.query(Quest).filter(Quest.journey_id == journey_id).all()
=======
def get_quests_by_end_date(db: Session, end_date: date) -> List[Quest]:
    return db.query(Quest).filter(Quest.end_date == end_date).all()

def get_active_quests(db: Session) -> List[Quest]:
    return db.query(Quest).filter(Quest.end_date.is_(None)).all()
>>>>>>> 67ed5e1 (changes to journey and quest crud for end data quiries)

def update_quest(db: Session, quest_id: int, quest_in: QuestUpdate) -> Optional[Quest]:
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        return None
    update_data = quest_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_quest, key, value)
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def delete_quest(db: Session, quest_id: int) -> Optional[Quest]:
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        return None
    db.delete(db_quest)
    db.commit()
    return db_quest