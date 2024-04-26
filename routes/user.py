from fastapi import APIRouter, Response, status
from db.mongodb import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

user = APIRouter()


@user.get("/users/{user_id}", response_model=User, tags=["users"])
def get_user(user_id: str):
    user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
    return userEntity(user)


@user.get('/users', response_model=List[User], tags=["users"])
def get_all_users():
    return usersEntity(conn.bancaria.users.find())


@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    id = conn.bancaria.users.insert_one(new_user).inserted_id
    user = conn.bancaria.users.find_one({"_id": id})
    return userEntity(user)


@user.put("/users/{user_id}", response_model=User, tags=["users"])
def update_user(user_id: str, user: User):
    updated_user = dict(user)
    del updated_user["id"]
    conn.bancaria.users.find_one_and_update(
        {"_id": ObjectId(user_id)}, {"$set": updated_user})
    user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
    return userEntity(user)


@user.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(user_id: str):
    conn.bancaria.users.find_one_and_delete({"_id": ObjectId(user_id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
