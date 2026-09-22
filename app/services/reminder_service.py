from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.reminder import Reminder
from models.task import Task


def create_reminder(
    db: Session,
    data,
    user_id: int
):
    task = (
        db.query(Task)
        .filter(Task.id == data.task_id)
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {data.task_id} does not exist"
        )

    reminder = Reminder(
        title=data.title,
        reminder_time=data.reminder_time,
        task_id=data.task_id,
        user_id=user_id
    )

    try:
        db.add(reminder)
        db.commit()
        db.refresh(reminder)
        return reminder
    except Exception:
        db.rollback()
        raise