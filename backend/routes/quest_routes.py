from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schema.quest_schema import QuestCreate, QuestRead, QuestUpdate
from schema.task_schema import TaskRead
from db import get_db
from crud.quest_crud import create_quest, get_quest, get_all_quests, update_quest, delete_quest, get_active_quests, get_quests_by_end_date
from crud.task_crud import get_tasks_by_quest
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

# read quests by end date
@router.get("/by-end-date/{end_date}", response_model=List[QuestRead])
async def read_quests_by_end_date(end_date: date, db: Session = Depends(get_db)):
    quests = get_quests_by_end_date(db, end_date)
    return [QuestRead.model_validate(quest) for quest in quests]

# read active quests (no end date)
@router.get("/active", response_model=List[QuestRead])
async def read_active_quests(db: Session = Depends(get_db)):
    quests = get_active_quests(db)
    return [QuestRead.model_validate(quest) for quest in quests]

# read tasks by quest id
@router.get("/tasks/{quest_id}", response_model=List[TaskRead])
async def read_tasks_by_quest(quest_id: int, db: Session = Depends(get_db)):
    tasks = get_tasks_by_quest(db, quest_id)
    return [TaskRead.model_validate(task) for task in tasks]

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