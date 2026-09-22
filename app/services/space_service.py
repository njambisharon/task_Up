from sqlalchemy.orm import Session
from repositories.space_repository import space_repository
from schemas.space import SpaceCreate
from models.space import Space

def create_space(db: Session,space_data: SpaceCreate,user_id:int):
    space = Space(
        name = space_data.name,
        description = space_data.description,
        user_id = user_id
    )
    return space_repository.create_space(db,space)

def get_spaces(db:Session,user_id:int):
    return space_repository.get_user_spaces(db,user_id)

def delete_space(db:Session,space_id:int):
    space = space_repository.get_space(db,space_id)
    if not space:
        raise ValueError("space not found")
    return space_repository.delete_space(db,space)
