from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.schema.entry_schema import EntryCreate, EntryRead, EntryUpdate
from backend.db import get_db
from backend.crud.entry_crud import create_entry, get_entry, get_all_entries, update_entry, delete_entry
from sqlalchemy.orm import Session

router = APIRouter(prefix="/entries", tags=["entries"])

# create
@router.post("/", response_model=EntryRead)
async def create_new_entry(entry_in: EntryCreate, db: Session = Depends(get_db)):
    entry = create_entry(db, entry_in)
    return EntryRead.model_validate(entry)

# read one
@router.get("/{entry_id}", response_model=EntryRead)
async def read_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = get_entry(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return EntryRead.model_validate(entry)

# read all
@router.get("/", response_model=List[EntryRead])
async def read_all_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = get_all_entries(db, skip=skip, limit=limit)
    return [EntryRead.model_validate(entry) for entry in entries]

# update
@router.put("/{entry_id}", response_model=EntryRead)
async def update_existing_entry(entry_id: int, entry_in: EntryUpdate, db: Session = Depends(get_db)):
    entry = update_entry(db, entry_id, entry_in)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return EntryRead.model_validate(entry)

# delete
@router.delete("/{entry_id}", response_model=EntryRead)
def delete_existing_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = delete_entry(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"message": "Entry deleted successfully"}