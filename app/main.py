from fastapi import FastAPI 
from database import Base,engine 
from models import user,space,task,reminder

app =FastAPI(
    title="TaskUp"
    
)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "messsage": "API is running"
    }
