from services.accountBank_service import AccountBankService
from models.accountBank import AccountBank
from typing import List


class AccountBankController:
    def __init__(self, account_service: AccountBankService):
        self.account_service = account_service


    def create_account(self, account: AccountBank) -> str:
        new_account = dict(account)
        created_account = self.account_service.create_account(new_account)
        return created_account

    def replace_balance(self, account_id: str, balance: float) -> AccountBank:
        updated_account = self.account_service.replace_balance(account_id, balance)
        return updated_account
    
    def update_balance(self, account_id: str, amount: float) -> str:
        updated_account = self.account_service.update_balance(account_id, amount)
        return updated_account
    
    def get_all_accounts(self) -> List[AccountBank]:
        accounts = self.account_service.get_all_accounts()
        return accounts
    
    def get_account(self, account_id: str) -> AccountBank:
        account = self.account_service.get_account(account_id)
        return account
    
    def delete_account(self, account_id: str) -> int:
        deleted_count = self.account_service.delete_account(account_id)
        return deleted_count
    
    def get_account_by_user(self, user_id: str) -> List[AccountBank]:
        accounts = self.account_service.get_account_by_user(user_id)
        return accounts

    # def __init__(self, user_service: UserService):
    #     self.user_service = user_service

    # def get_user(self, user_id: str) -> User:
    #     user = self.user_service.get_user(user_id)
    #     return user

    # def get_all_users(self) -> List[User]:
    #     users = self.user_service.get_all_users()
    #     return users

    # def create_user(self, user_data: User) -> User:
    #     new_user = dict(user_data)
    #     created_user = self.user_service.create_user(new_user)
    #     return created_user

    # def update_user(self, user_id: str, user: User) -> User:
    #     updated_user = self.user_service.update_user(user_id, user)
    #     return updated_user

    # def delete_user(self, user_id: str) -> int:
    #     deleted_count = self.user_service.delete_user(user_id)
    #     return deleted_count
