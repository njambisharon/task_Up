from sqlalchemy import Column ,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer,primary_key=True,index=True)
    title= Column(String,nullable=False)
    description = Column(String,nullable= True)
    status = Column(String ,nullable= False,default="pending")
    priority = Column (String,nullable=False,default="medium")

    user_id= Column(Integer,ForeignKey("users.id"),nullable=False)
    space_id = Column(Integer,ForeignKey("spaces.id"),nullable= True)

