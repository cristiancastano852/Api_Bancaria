from models.user import User
from db.mongodb import conn
from bson import ObjectId
from schemas.user import usersEntity, userEntity
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT


class UserService:
    def get_user(self, user_id: str):
        user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
        return userEntity(user)

    def get_all_users(self):
        return usersEntity(conn.bancaria.users.find())

    def create_user(self, user: dict):
        new_user_data = user
        del new_user_data["id"]
        result = conn.bancaria.users.insert_one(new_user_data)
        new_user = conn.bancaria.users.find_one({"_id": result.inserted_id})
        return userEntity(new_user)

    def update_user(self, user_id: str, user: User):
        updated_user_data = user.dict(exclude_unset=True)
        conn.bancaria.users.update_one({"_id": ObjectId(user_id)}, {
                                       "$set": updated_user_data})
        updated_user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
        return userEntity(updated_user)

    def delete_user(self, user_id: str):
        result = conn.bancaria.users.delete_one({"_id": ObjectId(user_id)})
        return Response(status_code=HTTP_204_NO_CONTENT)
