from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = "pending"
    priority: str
    space_id: int
    
class TaskUpdate(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None



class TaskResponse(BaseModel):

    id: int
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    user_id: int
    space_id: Optional[int] = None


    class Config:
        from_attributes = True