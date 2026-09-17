from sqlalchemy.orm import Session
from models.user import User
class UserRepository:
    def __init__(self):
        self.model = User

    def get(self,db:Session,user_id:int):
            return( db.query(self.model).filter(self.model.id==user_id).first())

    def get_all(self,db:Session):
         return db.query(self.model).all()
    def create_user(self,db:Session,data:dict):
        user = self.model(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def update (self,db:Session,db_obj:User,data:dict):
         for field,value in data.items():
              setattr(db_obj,field,value)

              db.commit()
              db.refresh(db_obj)

              return db_obj

    def delete(self,db:Session,db_obj:User):
         db.delete(db_obj)
         db.commit()
         return db_obj

user_repository = UserRepository()
    

