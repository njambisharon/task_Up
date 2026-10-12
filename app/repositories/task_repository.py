from sqlalchemy.orm import Session

from app.models.task import Task


def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_task_by_id(db: Session, task_id: int):
    return get_task(db, task_id)


def get_tasks(db: Session):
    return db.query(Task).all()


def get_user_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()


def update_task(db: Session, task: Task, data):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
    return task