from db.hash import Hash
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.schemas import UserBase
from db.models import User
from typing import List

def create_user(db: Session, request: UserBase)->User:
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session)->List[User]:
    return db.query(User).all()

def get_user(db: Session, id: int)->User:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} not found')
    return user

def get_user_by_username(db: Session, username: int)->User:
    user = db.query(User).filter(User.username == username).first()
    if not username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {username} not found')
    return user

def update_user(db: Session, id: int, request: UserBase)->bool:
    try:
        user = db.query(User).filter(User.id == id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with id {id} not found')
        user.update({
            User.username: request.username,
            User.email: request.email,
            User.password : Hash.bcrypt(request.password)
        })
        db.commit()
    except Exception as E:
        print(E)
        return False
    return True

def delete_user(db: Session, id: int)->bool:
    try:
        user = db.query(User).filter(User.id == id).first()
        db.delete(user)
        db.commit()
    except Exception as E:
        print(E)
        return False
    return True