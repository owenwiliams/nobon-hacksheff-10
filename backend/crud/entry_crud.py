import backend.schema.journey_schema as schema
import backend.models as models
import sqlalchemy.orm as Session
from typing import Optional, List

# create a new entry
def create_entry(db: Session, entry_in: schema.EntryCreate) -> models.Entry:
    db_entry = models.Entry(
        title=entry_in.title,
        body=entry_in.body,
        entry_date=entry_in.entry_date
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

# use models.Entry | None: if doesnt work???
def get_entry(db: Session, entry_id: int) -> Optional(models.Entry):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()

def get_all_entries(db: Session, skip: int = 0, limit: int = 100) -> List[models.Entry]:
    return db.query(models.Entry).offset(skip).limit(limit).all()

# update based on id
def update_entry(db: Session, entry_id: int, entry_in: schema.EntryUpdate) -> Optional(models.Entry):
    db_entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
    if not db_entry:
        return None
    if entry_in.title is not None:
        db_entry.title = entry_in.title
    if entry_in.body is not None:
        db_entry.body = entry_in.body
    if entry_in.entry_date is not None:
        db_entry.entry_date = entry_in.entry_date
    db.commit()
    db.refresh(db_entry)
    return db_entry

# delete based on id
def delete_entry(db: Session, entry_id: int) -> Optional(models.Entry]:
    db_entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
    if not db_entry:
        return None
    db.delete(db_entry)
    db.commit()
    return db_entry