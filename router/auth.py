import traceback
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse,UserLogin
from database import get_db
from models import User
from security import hash_password, verify_password

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def registration(userData: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(User).where(
            (User.email == userData.email)
        )
    ).scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    hashed_password = hash_password(userData.password)

    new_user = User(
        full_name=userData.full_name,
        email=userData.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        # "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email
        }
    }

@router.post("/login")
def login(userData: UserLogin, db: Session = Depends(get_db)):
    user = db.execute(
        select(User).where(User.email == userData.email) 
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(userData.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or password"
        )

    #NOW WE'LL GENERATE A TOKEN FOR THE USER AND RETURN IT IN THE RESPONSE USING python-jose.


    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email
        }
    }