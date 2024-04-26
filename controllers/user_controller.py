from services.user_service import UserService
from models.user import User
from typing import List


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id: str) -> User:
        try:
            user = self.user_service.get_user(user_id)
            return user
        except Exception as e:
            raise Exception("Error getting user: ", str(e))

    def get_all_users(self) -> List[User]:
        try:
            users = self.user_service.get_all_users()
            return users
        except Exception as e:
            raise Exception("Error getting all users: ", str(e))

    def create_user(self, user_data: User) -> User:
        try:
            new_user = dict(user_data)
            created_user = self.user_service.create_user(new_user)
            return created_user
        except Exception as e:
            raise Exception("Error creating user: ", str(e))

    def update_user(self, user_id: str, user: User) -> User:
        try:
            updated_user = self.user_service.update_user(user_id, user)
            return updated_user
        except Exception as e:
            raise Exception("Error updating user: ", str(e))

    def delete_user(self, user_id: str) -> int:
        try:
            deleted_count = self.user_service.delete_user(user_id)
            return deleted_count
        except Exception as e:
            raise Exception("Error deleting user: ", str(e))
