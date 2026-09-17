from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    description= Column(String,nullable=True)
    status = Column(String,nullable=False,default="pending")
    priority= Column (String,nullable=False,default= "meduim")

    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    space_id= Column(Integer,ForeignKey("spaces.id"),nullable=True)
    user = relationship("User",back_populates="tasks")
    space= relationship("Space",back_populates="tasks")
    reminders = relationship("Reminder",back_populates="task")
    