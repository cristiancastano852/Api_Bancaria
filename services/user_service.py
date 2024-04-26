from models.user import User
from db.mongodb import conn
from bson import ObjectId
from schemas.user import usersEntity, userEntity
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT


class UserService:
    def get_user(self, user_id: str):
        try:
            user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                return Response(status_code=404, detail=f"User with id <{user_id}> no found")
            return userEntity(user)
        except Exception as e:
            raise Exception("Error getting user: ", str(e))

    def get_all_users(self):
        try:
            return usersEntity(conn.bancaria.users.find())
        except Exception as e:
            raise Exception("Error getting all users: ", str(e))

    def create_user(self, user: dict):
        try:
            new_user_data = user
            del new_user_data["id"]
            result = conn.bancaria.users.insert_one(new_user_data)
            new_user = conn.bancaria.users.find_one(
                {"_id": result.inserted_id})
            return userEntity(new_user)
        except Exception as e:
            raise Exception("Error creating user: ", str(e))

    def update_user(self, user_id: str, user: User):
        try:
            updated_user_data = user.dict(exclude_unset=True)
            conn.bancaria.users.update_one({"_id": ObjectId(user_id)}, {
                                        "$set": updated_user_data})
            updated_user = conn.bancaria.users.find_one(
                {"_id": ObjectId(user_id)})
            if not updated_user:
                return Response(status_code=404, detail=f"User with id <{user_id}> no found")
            return userEntity(updated_user)
        except Exception as e:
            raise Exception("Error updating user: ", str(e))

    def delete_user(self, user_id: str):
        try:
            result = conn.bancaria.users.delete_one({"_id": ObjectId(user_id)})
            return Response(status_code=HTTP_204_NO_CONTENT)
        except Exception as e:
            raise Exception("Error deleting user: ", str(e))
