from services.user_service import UserService
from models.user import User
from typing import List
from fastapi import HTTPException


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id: str) -> User:
        """
        Retrieves a user with the specified user ID.

        Parameters:
        - user_id (str): The ID of the user to retrieve.

        Returns:
        - User: The user object representing the retrieved user.

        Raises:
        - HTTPException: If the user is not found or an error occurs while retrieving the user.
        - Exception: If an unexpected error occurs.
    """
        try:
            return self.user_service.get_user(user_id)
        except HTTPException as http_error:
            raise http_error
        except Exception as e:
            raise e

    def get_all_users(self) -> List[User]:
        """
        Returns a list of all users.

        Returns:
        - List[User]: A list of User objects representing all the users.

        Raises:
        - Exception: If an error occurs while retrieving the users.
        """
        try:
            users = self.user_service.get_all_users()
            return users
        except Exception as e:
            raise Exception("Error getting all users: ", str(e))

    def create_user(self, user_data: User) -> User:
        """
        Creates a new user with the provided user data.

        Parameters:
        - user_data (User): The user data to create the user.

        Returns:
        - User: The created user object.

        Raises:
        - Exception: If an error occurs while creating the user.
        """
        try:
            new_user = dict(user_data)
            created_user = self.user_service.create_user(new_user)
            return created_user

        except Exception as e:
            raise Exception("Error creating user: ", str(e))

    def update_user(self, user_id: str, user: User) -> User:
        """
        Updates a user with the specified user ID.

        Parameters:
        - user_id (str): The ID of the user to be updated.
        - user (User): The updated user object.

        Returns:
        - User: The updated user object.

        Raises:
        - Exception: If an error occurs while updating the user.
        """
        try:
            updated_user = self.user_service.update_user(user_id, user)
            return updated_user
        except Exception as e:
            raise Exception("Error updating user: ", str(e))

    def delete_user(self, user_id: str) -> int:
        """
        Deletes a user with the specified user ID.

        Parameters:
        - user_id (str): The ID of the user to be deleted.

        Returns:
        - int: The number of users deleted.

        Raises:
        - Exception: If an error occurs while deleting the user.
        """
        try:
            deleted_count = self.user_service.delete_user(user_id)
            return deleted_count
        except Exception as e:
            raise Exception("Error deleting user: ", str(e))
