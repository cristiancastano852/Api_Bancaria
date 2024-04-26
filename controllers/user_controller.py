from services.user_service import UserService
from models.user import User
from typing import List


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id: str) -> User:
        user = self.user_service.get_user(user_id)
        return user

    def get_all_users(self) -> List[User]:
        users = self.user_service.get_all_users()
        return users

    def create_user(self, user_data: User) -> User:
        new_user = dict(user_data)
        created_user = self.user_service.create_user(new_user)
        return created_user

    def update_user(self, user_id: str, user: User) -> User:
        updated_user = self.user_service.update_user(user_id, user)
        return updated_user

    def delete_user(self, user_id: str) -> int:
        deleted_count = self.user_service.delete_user(user_id)
        return deleted_count
