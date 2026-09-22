from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.space import SpaceCreate,SpaceResponse
from services import space_service

router = APIRouter (
    prefix= "/spaces",
    tags= ["spaces"]
)
@router.post("/",response_model= SpaceResponse)
def create_space(space:SpaceCreate,user_id:int,db:Session =Depends(get_db)):
    return space_service.create_space(db,space,user_id)

@router.get("/",response_model=list [SpaceResponse])
def get_spaces(user_id:int,db:Session = Depends(get_db)):
    return space_service.get_spaces(db,user_id)