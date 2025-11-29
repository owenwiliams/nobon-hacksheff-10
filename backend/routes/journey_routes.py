from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schema.journey_schema import JourneyCreate, JourneyRead, JourneyUpdate
from db import get_db
from crud.journey_crud import create_journey, get_journey, get_all_journeys, update_journey, delete_journey
from sqlalchemy.orm import Session

router = APIRouter(prefix="/journey", tags=["journey"])

# create
@router.post("/", response_model=JourneyRead)
async def create_new_journey(entry_in: JourneyCreate, db: Session = Depends(get_db)):
    entry = create_journey(db, entry_in)
    return JourneyRead.model_validate(entry)

# read one
@router.get("/{entry_id}", response_model=JourneyRead)
async def read_journey(entry_id: int, db: Session = Depends(get_db)):
    entry = get_journey(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Journey not found")
    return JourneyRead.model_validate(entry)

# read all
@router.get("/", response_model=List[JourneyRead])
async def read_all_journeys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = get_all_journeys(db, skip=skip, limit=limit)
    return [JourneyRead.model_validate(entry) for entry in entries]

# update
@router.put("/{entry_id}", response_model=JourneyRead)
async def update_existing_journey(entry_id: int, entry_in: JourneyUpdate, db: Session = Depends(get_db)):
    entry = update_journey(db, entry_id, entry_in)
    if not entry:
        raise HTTPException(status_code=404, detail="Journey not found")
    return JourneyRead.model_validate(entry)

# delete
@router.delete("/{entry_id}", response_model=JourneyRead)
def delete_existing_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = delete_journey(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Journey not found")
    return {"message": "Journey deleted successfully"}