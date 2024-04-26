from fastapi import APIRouter, Response, status
from controllers.accountBank_controller import AccountBankController
from services.accountBank_service import AccountBankService
from models.accountBank import AccountBank
from db.mongodb import conn
from typing import List

accountBank = APIRouter()
account_service = AccountBankService()
account_controller = AccountBankController(account_service)


@accountBank.get("/accounts/{account_id}", response_model=AccountBank, tags=["Bank Account"])
def get_account(account_id: str):
    return account_controller.get_account(account_id)


@accountBank.get('/accounts', response_model=List[AccountBank], tags=["Bank Account"])
def get_all_accounts():
    return account_controller.get_all_accounts()


@accountBank.post("/accounts", response_model=dict , tags=["Bank Account"])
def create_account(account: AccountBank):
    return account_controller.create_account(account)


@accountBank.put("/accounts/{account_id}", response_model=AccountBank, tags=["Bank Account"], description="Replace the balance of an account with the specified account_id.")
def replace_balance(account_id: str, balance: float):
    return account_controller.replace_balance(account_id, balance)


@accountBank.patch("/accounts/{account_id}", response_model=dict, tags=["Bank Account"], description="Increase or decrease the balance of an account if the amount is positive or negative, respectively.")
def update_balance(account_id: str, amount: float):
    return account_controller.update_balance(account_id, amount)


@accountBank.delete("/accounts/{account_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Bank Account"])
def delete_account(account_id: str):
    return account_controller.delete_account(account_id)


@accountBank.get("/accounts/user/{user_id}", response_model=List[AccountBank], tags=["Bank Account"])
def get_account_by_user(user_id: str):
    return account_controller.get_account_by_user(user_id)
