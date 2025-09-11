from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app import models
from app.routes import tasks

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

app.include_router(tasks.router)