from sqlalchemy.orm import Session
from models.task import Task


def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks(db: Session):
    return db.query(Task).all()
def get_user_tasks(db, user_id):
    return db.query(Task).filter(
        Task.user_id == user_id
    ).all()