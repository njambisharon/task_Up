from sqlalchemy.orm import Session
from models.reminder import Reminder

class ReminderRepository:
    def __init__(self):
        self.model = Reminder
    def get(self,db:Session,reminder_id:int):
        return (db.query(self.model).filter(self.model.id==reminder_id).first())
    def get_all(self,db:Session):
        return db.query(self.model).all()
    def create_reminder(self,db:Session,data:dict):
        reminder = self.model(**data)
        db.add(reminder)
        db.commit()
        db.refresh(reminder)
        return reminder
    def update (self,db:Session,db_obj: Reminder,data:dict):
        for field ,value in data.items():
            setattr(db_obj,field,value)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        def delete(self,db:Session,db_obj:Reminder):
            db.delete(db_obj)
            db.commit()

            return db_obj
        reminder_repository = ReminderRepository()
            