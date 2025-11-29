from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schema.quest_schema import QuestCreate, QuestRead, QuestUpdate
from db import get_db
from crud.quest_crud import create_quest, get_quest, get_all_quests, update_quest, delete_quest
from sqlalchemy.orm import Session
    
router = APIRouter(prefix="/quests", tags=["quests"])

# create
@router.post("/", response_model=QuestRead)
async def create_new_quest(quest_in: QuestCreate, db: Session = Depends(get_db)):
    quest = create_quest(db, quest_in)
    return QuestRead.model_validate(quest)

# read one
@router.get("/{quest_id}", response_model=QuestRead)
async def read_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = get_quest(db, quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return QuestRead.model_validate(quest)

# read all
@router.get("/", response_model=List[QuestRead])
async def read_all_quests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quests = get_all_quests(db, skip=skip, limit=limit)
    return [QuestRead.model_validate(quest) for quest in quests]

# update
@router.put("/{quest_id}", response_model=QuestRead)
async def update_existing_quest(quest_id: int, quest_in: QuestUpdate, db: Session = Depends(get_db)):
    quest = update_quest(db, quest_id, quest_in)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return QuestRead.model_validate(quest)

# delete
@router.delete("/{quest_id}", response_model=QuestRead)
def delete_existing_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = delete_quest(db, quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return {"message": "Quest deleted successfully"}