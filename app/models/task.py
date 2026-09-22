from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    space_id = Column(Integer, ForeignKey("spaces.id"),nullable= True)

    user = relationship("User",back_populates="tasks")

    space = relationship("Space",back_populates="tasks")

    reminders = relationship("Reminder", back_populates="task",cascade="all, delete"
    )