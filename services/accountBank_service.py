from datetime import datetime
from db.mongodb import conn
from bson import ObjectId
from schemas.accountBack import accountsEntity, accountEntity
from fastapi import Response
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.exceptions import HTTPException


class AccountBankService:
    def is_valid_objectid(cls, user_id: str):
        """
        Check if the provided user_id is a valid ObjectId.

        Parameters:
            user_id (str): The user_id to be checked.

        Returns:
            bool: True if the user_id is a valid ObjectId, False otherwise.
        """
        try:
            ObjectId(user_id)
            return True
        except Exception:
            return False

    def create_account(self, new_account_data: dict):
        """
        Create a new account with the provided account data.

        Parameters:
            new_account_data (dict): A dictionary containing the data for the new account.

        Returns:
            dict: A dictionary containing the ID of the newly created account.

        Raises:
            HTTPException: If the user with the specified user_id is not found or if there is an error during the account creation process.
        """
        try:
            del new_account_data["id"]
            user_id = new_account_data["user_id"]
            if not self.is_valid_objectid(user_id):
                raise HTTPException(
                    status_code=404, detail=f"User with id <{user_id}> no found")
            user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                raise HTTPException(
                    status_code=404, detail=f"User with id <{user_id}> no found")
            result = conn.bancaria.accounts.insert_one(new_account_data)
            inserted_id = result.inserted_id
            return {"id": str(inserted_id)}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise Exception("Error creating account ", str(e))

    def replace_balance(self, account_id: str, balance: float):
        """
        Replace the balance of an account with the specified account_id.

        Parameters:
            account_id (str): The unique identifier of the account.
            balance (float): The new balance to be set for the account.

        Returns:
            accountEntity: An object representing the updated account with the modified balance.

        Raises:
            HTTPException: If the account with the specified account_id is not found.
        """
        try:
            update_data = {
                "balance": balance,
                "updated_at": datetime.now()  # Update the updated_at field
            }
            conn.bancaria.accounts.update_one({"_id": ObjectId(account_id)}, {
                "$set": update_data})
            updated_account = conn.bancaria.accounts.find_one(
                {"_id": ObjectId(account_id)})
            return accountEntity(updated_account)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_balance(self, account_id: str, balance_change: float):
        """
        if the balance_change is positive, the balance will be increased.
        if the balance_change is negative, the balance will be decreased.
        Update the balance of an account with the specified account_id.

        Parameters:
            account_id (str): The unique identifier of the account.
            balance_change (float): The amount by which the balance should be changed.

        Returns:
            accountEntity: An object representing the updated account with the new balance.

        Raises:
            HTTPException: If the account with the specified account_id is not found.
        """
        try:
            account = conn.bancaria.accounts.find_one(
                {"_id": ObjectId(account_id)})
            if account:
                new_balance = account["balance"] + balance_change
                update_data = {
                    "balance": new_balance,
                    "updated_at": datetime.now()
                }
                conn.bancaria.accounts.update_one(
                    {"_id": ObjectId(account_id)}, {"$set": update_data})
                updated_account = conn.bancaria.accounts.find_one(
                    {"_id": ObjectId(account_id)})
                return {"Saldo actualizado": accountEntity(updated_account)}
            else:
                raise HTTPException(
                    status_code=404, detail="Account not found")
        except Exception as e:
            raise Exception("Error updating balance: ", str(e))

    def get_all_accounts(self):
        return accountsEntity(conn.bancaria.accounts.find())

    def get_account(self, account_id: str):
        """
        Get the account with the specified account_id.

        Parameters:
            account_id (str): The unique identifier of the account.

        Returns:
            dict: A dictionary representing the account with the specified account_id.

        Raises:
            HTTPException: If the account with the specified account_id is not found.
            Exception: If there is an error getting the account.
        """
        try:
            account = conn.bancaria.accounts.find_one(
                {"_id": ObjectId(account_id)})
            if not account:
                raise HTTPException(
                    status_code=404, detail="Account not found")
            return accountEntity(account)
        except Exception as e:
            raise Exception("Error getting account: ", str(e))

    def get_account_by_user(self, user_id: str):
        """
        Get all accounts associated with a user.

        Parameters:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list of accountEntity objects representing the accounts associated with the user.

        Raises:
            Exception: If there is an error retrieving the accounts.
        """
        try:
            accounts = conn.bancaria.accounts.find({"user_id": user_id})
            return accountsEntity(accounts)
        except Exception as e:
            raise Exception("Error getting accounts: ", str(e))

    def delete_account(self, account_id: str):
        """
        Delete an account with the specified account_id.

        Parameters:
            account_id (str): The unique identifier of the account to be deleted.

        Returns:
            Response: A response indicating the success or failure of the deletion operation.

        Raises:
            HTTPException: If the account with the specified account_id is not found.
            Exception: If there is an error during the deletion process.
        """
        try:
            result = conn.bancaria.accounts.delete_one(
                {"_id": ObjectId(account_id)})
            if result.deleted_count == 0:
                raise HTTPException(
                    status_code=404, detail="Account not found")
            return Response(status_code=HTTP_204_NO_CONTENT)
        except HTTPException as e:
            raise e
        except Exception as e:
            raise Exception("Error deleting account: ", str(e))
