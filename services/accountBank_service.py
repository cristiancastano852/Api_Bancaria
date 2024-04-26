from datetime import datetime
from models.accountBank import AccountBank
from db.mongodb import conn
from bson import ObjectId
from schemas.accountBack import accountsEntity, accountEntity
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.exceptions import HTTPException


class AccountBankService:
    def is_valid_objectid(cls, user_id: str):
        try:
            ObjectId(user_id)
            return True
        except Exception:
            return False
    
    def create_account(self, new_account_data: dict):
        del new_account_data["id"]
        user_id = new_account_data["user_id"]
        if not self.is_valid_objectid(user_id):
            raise HTTPException(status_code=404, detail=f"Usuario con el id <{user_id}> no encontrado")
        user = conn.bancaria.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail=f"Usuario con el id <{user_id}> no encontrado")
        result = conn.bancaria.accounts.insert_one(new_account_data)
        inserted_id = result.inserted_id
        return {"id": str(inserted_id)}

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
        update_data = {
            "balance": balance,
            "updated_at": datetime.now()  # Update the updated_at field
        }
        conn.bancaria.accounts.update_one({"_id": ObjectId(account_id)}, {
                                          "$set": update_data})
        updated_account = conn.bancaria.accounts.find_one(
            {"_id": ObjectId(account_id)})
        return accountEntity(updated_account)

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
            raise HTTPException(status_code=404, detail="Cuenta no encontrada")

    def get_all_accounts(self):
        return accountsEntity(conn.bancaria.accounts.find())

    def get_account(self, account_id: str):
        account = conn.bancaria.accounts.find_one(
            {"_id": ObjectId(account_id)})
        return accountEntity(account)

    def get_account_by_user(self, user_id: str):
        accounts = conn.bancaria.accounts.find({"user_id": user_id})
        return accountsEntity(accounts)

    def delete_account(self, account_id: str):
        result = conn.bancaria.accounts.delete_one(
            {"_id": ObjectId(account_id)})
        return Response(status_code=HTTP_204_NO_CONTENT)
