from fastapi import APIRouter
from db.mongodb import conn
from schemas.user import userEntity, usersEntity
from models.user import User

# Creamos una instancia de APIRouter
user = APIRouter()

@user.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@user.get("/users/")
def get_all_users():
    return usersEntity(conn.local.users.find())

@user.post("/users/")
def create_user(user: User):
    new_user = dict(user)
    id= conn.local.users.insert_one(new_user).inserted_id
    return str(id)

@user.put("/users/{user_id}")
def update_user(user_id: int):
    return {"user_id": user_id}

@user.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id}
