from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend import models, schema

def create_entry(db: Session, entry_in: schema.EntryCreate) -> models.Entry:
    # Verify progress exists (foreign key)
    progress = db.query(models.Progress).filter(models.Progress.id == entry_in.progress_id).first()
    if progress is None:
        raise HTTPException(status_code=404, detail=f"Progress id {entry_in.progress_id} not found")

    db_entry = models.Entry(**entry_in.model_dump())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_entry(db: Session, entry_id: int) -> Optional[models.Entry]:
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()

def get_entries(db: Session, skip: int = 0, limit: int = 100) -> List[models.Entry]:
    return db.query(models.Entry).offset(skip).limit(limit).all()

def get_entries_by_progress(db: Session, progress_id: int, skip: int = 0, limit: int = 100) -> List[models.Entry]:
    return (
        db.query(models.Entry)
        .filter(models.Entry.progress_id == progress_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_entry(db: Session, entry_id: int, entry_in: schema.EntryUpdate) -> Optional[models.Entry]:
    db_entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
    if db_entry is None:
        return None

    update_data = entry_in.model_dump(exclude_unset=True)

    # If progress_id is being changed, ensure the new progress exists
    if "progress_id" in update_data:
        progress = db.query(models.Progress).filter(models.Progress.id == update_data["progress_id"]).first()
        if progress is None:
            raise ValueError(f"Progress id {update_data['progress_id']} not found")

    for key, value in update_data.items():
        setattr(db_entry, key, value)

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_entry(db: Session, entry_id: int) -> Optional[models.Entry]:
    db_entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
    if db_entry is None:
        return None

    db.delete(db_entry)
    db.commit()
    return db_entry