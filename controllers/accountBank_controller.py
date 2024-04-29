from services.accountBank_service import AccountBankService
from models.accountBank import AccountBank
from typing import List


class AccountBankController:
    def __init__(self, account_service: AccountBankService):
        self.account_service = account_service

    def create_account(self, account: AccountBank) -> str:
        """
        Create a new account.

        Parameters:
        - account (AccountBank): The AccountBank object representing the account to be created.

        Returns:
        - str: The ID of the newly created account.

        """
        new_account = dict(account)
        created_account = self.account_service.create_account(new_account)
        return created_account

    def replace_balance(self, account_id: str, balance: float) -> AccountBank:
        """
        Replace the balance of an account.

        Parameters:
        - account_id (str): The ID of the account to replace the balance.
        - balance (float): The new balance to replace the current balance.

        Returns:
        - AccountBank: The updated AccountBank object representing the account with the replaced balance.

        """
        updated_account = self.account_service.replace_balance(
            account_id, balance)
        return updated_account

    def update_balance(self, account_id: str, amount: float) -> str:
        """
        Update the balance of an account.

        Parameters:
        - account_id (str): The ID of the account to update.
        - amount (float): The amount by which to update the balance.

        Returns:
        - str: The updated account information.

        """
        updated_account = self.account_service.update_balance(
            account_id, amount)
        return updated_account

    def get_all_accounts(self) -> List[AccountBank]:
        """
        Get all accounts.

        Returns:
        - List[AccountBank]: A list of AccountBank objects representing all the accounts.

        """
        accounts = self.account_service.get_all_accounts()
        return accounts

    def get_account(self, account_id: str) -> AccountBank:
        """
        Get an account by its ID.

        Parameters:
        - account_id (str): The ID of the account to retrieve.

        Returns:
        - AccountBank: The AccountBank object representing the account with the specified ID.

        """
        account = self.account_service.get_account(account_id)
        return account

    def delete_account(self, account_id: str) -> int:
        """
        Delete an account.

        Parameters:
        - account_id (str): The ID of the account to be deleted.

        Returns:
        - int: The number of accounts deleted (should be 1 if successful).

        """
        deleted_count = self.account_service.delete_account(account_id)
        return deleted_count

    def get_account_by_user(self, user_id: str) -> List[AccountBank]:
        """
        Get all accounts associated with a specific user.

        Parameters:
        - user_id (str): The ID of the user.

        Returns:
        - List[AccountBank]: A list of AccountBank objects representing the accounts associated with the user.

        """
        accounts = self.account_service.get_account_by_user(user_id)
        return accounts
