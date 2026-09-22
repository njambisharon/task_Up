from sqlalchemy import Column ,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Space(Base):
    __tablename__ ="spaces"

    id = Column(Integer,primary_key=True ,index=True,autoincrement=True)
    name = Column(String)
    description= Column(String,nullable=True)

    user_id= Column(Integer,ForeignKey("users.id"),nullable=False)
    user = relationship("User",back_populates="spaces")
    tasks = relationship("Task", back_populates="space")
    reminders = relationship("Reminder", back_populates="space")
    