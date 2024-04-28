from models.user import User
from db.mongodb import conn
from bson import ObjectId
from schemas.user import usersEntity, userEntity
from fastapi import Response, HTTPException
from starlette.status import HTTP_204_NO_CONTENT


class UserService:
    def get_user(self, user_id: str):
        """
        Retrieve a user by their ID.

        :param user_id: The ID of the user to retrieve.
        :return: The user object.
        """
        user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(
                status_code=404, detail=f"User with id <{user_id}> no found")
        return userEntity(user)

    def get_all_users(self):
        """
        Retrieve all users.

        :return: A list of user objects.
        :raises Exception: If there is an error retrieving the users.
        """
        try:
            return usersEntity(conn.bancaria.users.find())
        except Exception as e:
            raise Exception("Error getting all users: ", str(e))

    def create_user(self, user: dict):
        """
        Create a new user.

        :param user: A dictionary containing the user data.
        :return: The created user object.
        :raises Exception: If there is an error creating the user.
        """
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
        """
        Update a user by their ID.

        :param user_id: The ID of the user to update.
        :param user: The updated user object.
        :return: The updated user object.
        :raises Exception: If there is an error updating the user.
        """
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
        """
        Delete a user by their ID.

        :param user_id: The ID of the user to delete.
        :return: A Response object with status code 204 (No Content) indicating successful deletion.
        :raises Exception: If there is an error deleting the user.
        """
        try:
            result = conn.bancaria.users.delete_one({"_id": ObjectId(user_id)})
            return Response(status_code=HTTP_204_NO_CONTENT)
        except Exception as e:
            raise Exception("Error deleting user: ", str(e))
