from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.reminder import ReminderCreate, ReminderResponse
from services import reminder_service

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post("/", response_model=ReminderResponse)
def create_reminder(
    reminder: ReminderCreate,
    db: Session = Depends(get_db)
):
    return reminder_service.create_reminder(
        db=db,
        data=reminder,
      
    )