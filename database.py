from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

URL_DATABASE = os.getenv("DATABASE_URL")

if not URL_DATABASE:
    raise RuntimeError("DATABASE_URL is not configured")

#connection established
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(bind=engine)


#dependency function for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass