from sqlalchemy.orm import Session
from models.task import Task

class TaskRepository:
    def __init__ (self):
        self.model = Task 
    def get (self,db:Session,task_id:int):
        return (db.query(self.model).filter(self.model.id ==task_id).fisrt())  
    def get_all(self,db:Session):
        return db.query(self.model).all()
    def create_task(self,db:Session,data:dict):
        task = self.model(**data)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    def update(self,db:Session,db_obj:Task,data:dict):
         for field,value in data.items():
             
            setattr(db_obj,field,value)
            db.commit()
            db.refresh (db_obj)
            return db_obj
task_repository = TaskRepository
