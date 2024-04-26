from fastapi import APIRouter, Response, status, HTTPException
from controllers.user_controller import UserController
from services.user_service import UserService
from models.user import User
from db.mongodb import conn
from typing import List

user = APIRouter()
user_service = UserService()
user_controller = UserController(user_service)


@user.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: str):
    try:
        return user_controller.get_user(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@user.get('/users', response_model=List[User], tags=["Users"])
def get_all_users():
    return user_controller.get_all_users()


@user.post("/users", response_model=User, tags=["Users"])
def create_user(user: User):
    try:
        return user_controller.create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@user.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: str, user: User):
    try:
        return user_controller.update_user(user_id, user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@user.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: str):
    try:
        return user_controller.delete_user(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
