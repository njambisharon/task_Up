from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.reminder import ReminderCreate, ReminderResponse
from app.services import reminder_service

router = APIRouter(prefix="/reminders", tags=["Reminders"])


@router.post("/", response_model=ReminderResponse)
def create_reminder(
    reminder: ReminderCreate,
    user_id: int,
    db: Session = Depends(get_db),
):
    return reminder_service.create_reminder(db=db, data=reminder, user_id=user_id)