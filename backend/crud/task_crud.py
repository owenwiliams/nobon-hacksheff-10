from typing import List, Optional
from sqlalchemy.orm import Session
from models import Task
from schema.task_schema import TaskCreate, TaskUpdate
    
def create_task(db: Session, task_in: TaskCreate) -> Task:
    db_task = Task(**task_in.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[Task]:
    return db.query(Task).offset(skip).limit(limit).all()

def get_tasks_by_quest(db: Session, quest_id: int) -> List[Task]:
    return db.query(Task).filter(Task.quest_id == quest_id).all()

def update_task(db: Session, task_id: int, task_in: TaskUpdate) -> Optional[Task]:
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        return None
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> Optional[Task]:
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        return None
    db.delete(db_task)
    db.commit()
    return db_task