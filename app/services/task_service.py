from sqlalchemy.orm import Session
from repositories import task_repository
from schemas.task import TaskCreate, TaskUpdate
from models.task import Task

def create_task(db:Session,task_data: TaskCreate,user_id:int):
    task = Task(
    title=task_data.title,
    description=task_data.description,
    status=task_data.status or "pending",
    priority=task_data.priority,
    user_id=user_id,
    space_id=task_data.space_id
)
   
    return task_repository.create_task(db,task)
def get_tasks(
        db:Session,
        user_id:int
):
    return task_repository.get_user_tasks(db,user_id)
def update_task(db:Session,task_id:int,task_data:TaskUpdate):
    task = task_repository.get_task(db,task_id)
    if not task:
        raise ValueError("Task not found")
    return task_repository.update_task(db,task,task_data)
def delete_task(
        db: Session,
        task_id:int
):
    task= task_repository.get_task(db,task_id)
    if not task :
        raise ValueError("Task not found")
    return task_repository.delete_task(
        db,
        task
    )
   

