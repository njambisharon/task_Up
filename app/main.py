from fastapi import FastAPI 
from database import Base,engine 
from models import user, task, space, reminder
from routers import  users,tasks,spaces,reminders

app =FastAPI(
    title="TaskUp"
    
)


app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(spaces.router)
app.include_router(reminders.router)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "messsage": "API is running"
    }



