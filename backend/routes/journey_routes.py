from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import date
from schema.journey_schema import JourneyCreate, JourneyRead, JourneyUpdate
from schema.quest_schema import QuestRead
from db import get_db
from crud.journey_crud import create_journey, get_journey, get_all_journeys, update_journey, delete_journey, get_journeys_by_end_date, get_active_journeys
from crud.quest_crud import get_quests_by_journey
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

# read quests by journey id
@router.get("/quests/{journey_id}", response_model=List[QuestRead])
async def read_quests_by_journey(journey_id: int, db: Session = Depends(get_db)):
    quests = get_quests_by_journey(db, journey_id)
    return [QuestRead.model_validate(quest) for quest in quests]

# read journeys by end date
@router.get("/by-end-date/{end_date}", response_model=List[JourneyRead])
async def read_journeys_by_end_date(end_date: date, db: Session = Depends(get_db)):
    journeys = get_journeys_by_end_date(db, end_date)
    return [JourneyRead.model_validate(journey) for journey in journeys]

# read active journeys (no end date)
@router.get("/active", response_model=List[JourneyRead])
async def read_active_journeys(db: Session = Depends(get_db)):
    journeys = get_active_journeys(db)
    return [JourneyRead.model_validate(journey) for journey in journeys]



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