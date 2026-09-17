from sqlalchemy.orm import Session
from models.space import Space

class SpaceRepository:
    def __init__(self):
        self.model =Space

    def get (self,db:Session,space_id:int):
            return (db.query(self.model).filter(self.model.id ==space_id).first())

    def get_all(self,db:Session):
         return db.query(self.model).all()

    def create_space(self,db:Session,data:dict):
         space = self.model(**data)
         db.add(space)
         db.commit()
         db.refresh(space)
         return space

    def update(self,db:Session,db_obj:Space,data:dict):
         for field ,value in data.items():
              setattr (db_obj,field,value)
              db.commit()
              db.refresh(db_obj)

              return db_obj

    def delete(self,db:Session,db_obj:Space):
         db.delete(db_obj)
         db.commit ()
         return db_obj     
space_repository = SpaceRepository    