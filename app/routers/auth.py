

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def create_account(user: schemas.CreateAccount, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password


    user_exist = db.query(models.User).filter(models.User.email == user.email).first()

    if user_exist == None:
        print()
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()

        # this returns back the post
        db.refresh(new_user)
        return new_user
    
    # fix status code
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists")


# @router.post("/login", response_model=schema.Login)
# def login()