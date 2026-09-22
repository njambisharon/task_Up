from fastapi import APIRouter ,Depends,HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.task import TaskCreate, TaskResponse,TaskUpdate
from services import task_service

router = APIRouter(
    prefix= "/tasks",
    tags = ["Tasks"]
)
@router.post ("/",response_model=TaskResponse)
def create_task(task: TaskCreate,user_id:int,db:Session=Depends(get_db)):
    return task_service.create_task(db,task,user_id)
@router.get("/",response_model= list[TaskResponse])

def get_tasks(user_id:int,db:Session=Depends(get_db)):
    return task_service.get_tasks(db,user_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int,task: TaskUpdate,db: Session = Depends(get_db)):
    try:
        return task_service.update_task(db,task_id,task)

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
@router.delete("/{task_id}")
def delete_task(task_id: int,db: Session = Depends(get_db)):
    return task_service.delete_task(db,task_id)
    