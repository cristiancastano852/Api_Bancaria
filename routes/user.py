from fastapi import APIRouter, Response, status
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
    return user_controller.get_user(user_id)

@user.get('/users', response_model=List[User], tags=["Users"])
def get_all_users():
    return user_controller.get_all_users()

@user.post("/users", response_model=User, tags=["Users"])
def create_user(user: User):
    return user_controller.create_user(user)

@user.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: str, user: User):
    return user_controller.update_user(user_id, user)

@user.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: str):
    return user_controller.delete_user(user_id)
