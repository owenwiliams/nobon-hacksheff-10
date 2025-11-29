from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.schema.task_schema import TaskCreate, TaskRead, TaskUpdate
from backend.db import get_db
from backend.crud.task_crud import create_task, get_task, get_all_tasks, update_task, delete_task
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])

# create
@router.post("/", response_model=TaskRead)
async def create_new_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    task = create_task(db, task_in)
    return TaskRead.model_validate(task)

# read one
@router.get("/{task_id}", response_model=TaskRead)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead.model_validate(task)

# read all
@router.get("/", response_model=List[TaskRead])
async def read_all_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = get_all_tasks(db, skip=skip, limit=limit)
    return [TaskRead.model_validate(task) for task in tasks]

# update
@router.put("/{task_id}", response_model=TaskRead)
async def update_existing_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead.model_validate(task)

# delete
@router.delete("/{task_id}", response_model=TaskRead)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}