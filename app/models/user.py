from sqlalchemy import Column ,Integer ,String ,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id= Column(Integer,primary_key= True,index=True)
    username = Column (String,nullable=False)
    email =Column(String,nullable=False,unique=True,index=True)
    password= Column(String,nullable=False)

    tasks = relationship("Task",back_populates="user")
    spaces = relationship("Space",back_populates="user")
    reminders= relationship("Reminder",back_populates="user")
