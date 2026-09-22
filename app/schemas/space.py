from pydantic import BaseModel
from typing import Optional


class SpaceCreate(BaseModel):
    name: str
    description: Optional [str] = None

class  SpaceResponse(BaseModel):
    id: int 
    name: str
    description: Optional[str]
    user_id: int
class Config:
    from_attributes = True    