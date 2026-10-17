from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()  # Load environment variables from .env file

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

#Now we'll have the functions to hash the password
def hash_password(plain_password: str) -> str:
    #hash the password using bcrypt (hashed + salt) and returns it
    return password_context.hash(plain_password) 

#Now that we have the hashed value we can't unhash it, but we can verify it using the verify function
def verify_password(plain_password: str, hashed_password: str) -> bool:
    #verify the password using bcrypt and returns True or False
    return password_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    #This function will create a JWT token using the data provided and returns it
    #We'll use the python-jose library to create the token
    data_to_encode = data.copy()

    expiration_date = datetime.now(timezone.utc) + timedelta(minutes=30)  # Token expires in 30 minutes

    data_to_encode.update({"exp": expiration_date})

    token = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

    
    