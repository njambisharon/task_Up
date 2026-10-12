from fastapi import FastAPI

from app.database import Base, engine
from app.routers import reminders, spaces, tasks, users

app = FastAPI(title="TaskUp")

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(spaces.router)
app.include_router(reminders.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}


