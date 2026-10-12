from pydantic import BaseModel, ConfigDict


class SpaceCreate(BaseModel):
    name: str
    description: str | None = None


class SpaceResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    user_id: int

    model_config = ConfigDict(from_attributes=True)