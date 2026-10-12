from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ReminderCreate(BaseModel):
    title: str
    reminder_time: datetime
    task_id: Optional[int] = None


class ReminderResponse(BaseModel):
    id: int
    title: str
    reminder_time: datetime

    model_config = ConfigDict(from_attributes=True)