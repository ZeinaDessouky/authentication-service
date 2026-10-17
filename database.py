from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
import os

URL_DATABASE = os.getenv("DATABASE_URL")

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