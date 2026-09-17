from sqlalchemy import Column ,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Space(Base):
    __tablename__ ="spaces"

    id = Column(Integer,primary_key=True ,index=True)
    name = Column(String)
    description= Column(String,nullable=True)

    user_id= Column(Integer,ForeignKey("users.id"),nullable=False)
    user = relationship("User",back_populates="spaces")
    tasks = relationship("Space", back_populates="user")