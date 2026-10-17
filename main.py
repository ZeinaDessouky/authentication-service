from fastapi import FastAPI
from database import Base, engine
from models import User
from database import get_db
from sqlalchemy.orm import Session
from router import auth

app = FastAPI()

app.include_router(auth.router)

Base.metadata.create_all(bind=engine)
# db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def root():
    return {"message": "Authentication Service in Progress"}

# @app.get("/zoz")
# async def root():
#     return {"message": "zanzun is happy"} #Just experimenting

@app.get("/home")
async def home():
    return {"message": "Welcome to the Authentication Service!"}

@app.get("/about")
async def about():
    return {"message": "This is the Authentication Service API. It provides endpoints for user authentication and management.",
            "creator": "Zeina", 
            "company": "Duckurity",
            "version": "1.0.0"}
