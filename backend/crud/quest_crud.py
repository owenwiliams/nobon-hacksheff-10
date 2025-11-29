from typing import List, Optional
from sqlalchemy.orm import Session
from backend import models, schema

def create_quest(db: Session, quest_in: schema.QuestCreate) -> models.Quest:
    db_quest = models.Quest(**quest_in.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def get_quest(db: Session, quest_id: int) -> Optional[models.Quest]:
    return db.query(models.Quest).filter(models.Quest.id == quest_id).first()

def get_all_quests(db: Session, skip: int = 0, limit: int = 100) -> List[models.Quest]:
    return db.query(models.Quest).offset(skip).limit(limit).all()

def update_quest(db: Session, quest_id: int, quest_in: schema.QuestUpdate) -> Optional[models.Quest]:
    db_quest = db.query(models.Quest).filter(models.Quest.id == quest_id).first()
    if db_quest is None:
        return None
    update_data = quest_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_quest, key, value)
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def delete_quest(db: Session, quest_id: int) -> Optional[models.Quest]:
    db_quest = db.query(models.Quest).filter(models.Quest.id == quest_id).first()
    if db_quest is None:
        return None
    db.delete(db_quest)
    db.commit()
    return db_quest