from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import book, author, client
from app.routers import book_router, author_router, client_router

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include routers
app.include_router(book_router.router)
app.include_router(author_router.router)
app.include_router(client_router.router)