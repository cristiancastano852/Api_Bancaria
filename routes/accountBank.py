from fastapi import APIRouter, Response, status, HTTPException
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
    """
    Get account details by account ID.

    Parameters:
    - account_id (str): The ID of the account.

    Returns:
    - AccountBank: The account details.

    Raises:
    - HTTPException: If the account is not found.

    """
    try:
        return account_controller.get_account(account_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@accountBank.get('/accounts', response_model=List[AccountBank], tags=["Bank Account"])
def get_all_accounts():
    """
    Get all bank accounts.

    Returns a list of all bank accounts.

    Raises:
        HTTPException: If there is an internal server error.

    Returns:
        List[AccountBank]: A list of bank accounts.

    """
    try:
        return account_controller.get_all_accounts()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@accountBank.post("/accounts", response_model=dict, tags=["Bank Account"])
def create_account(account: AccountBank):
    """
    Create a new bank account.

    Parameters:
    - account (AccountBank): The account details.

    Returns:
    - dict: The created account details.

    Raises:
    - HTTPException: If there is an HTTP error.
    - HTTPException: If there is an internal server error.

    """
    try:
        return account_controller.create_account(account)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@accountBank.put("/accounts/{account_id}", response_model=AccountBank, tags=["Bank Account"], description="Replace the balance of an account with the specified account_id.")
def replace_balance(account_id: str, balance: float):
    """
    Replace the balance of an account with the specified account_id.

    Parameters:
    - account_id (str): The ID of the account to replace the balance.
    - balance (float): The new balance to replace.

    Returns:
    - AccountBank: The updated account with the replaced balance.

    Raises:
    - HTTPException: If there is an error while replacing the balance.

    """
    try:
        return account_controller.replace_balance(account_id, balance)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@accountBank.patch("/accounts/{account_id}", response_model=dict, tags=["Bank Account"], description="Increase or decrease the balance of an account if the amount is positive or negative, respectively.")
def update_balance(account_id: str, amount: float):
    """
    Increase or decrease the balance of an account if the amount is positive or negative, respectively.

    Parameters:
    - account_id (str): The ID of the account to update the balance.
    - amount (float): The amount by which to increase or decrease the balance.

    Returns:
    - dict: A dictionary containing the updated account information.

    Raises:
    - HTTPException: If there is an error updating the balance.

    """
    try:
        return account_controller.update_balance(account_id, amount)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@accountBank.delete("/accounts/{account_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Bank Account"])
def delete_account(account_id: str):
    """
    Deletes a bank account.

    Parameters:
    - account_id (str): The ID of the account to be deleted.

    Returns:
    - None

    Raises:
    - HTTPException: If there is an HTTP error during the deletion process.
    - HTTPException: If there is an internal server error during the deletion process.
    """
    try:
        return account_controller.delete_account(account_id)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@accountBank.get("/accounts/user/{user_id}", response_model=List[AccountBank], tags=["Bank Account"])
def get_account_by_user(user_id: str):
    """
    Get all bank accounts associated with a user.

    Parameters:
    - user_id (str): The ID of the user.

    Returns:
    - List[AccountBank]: A list of AccountBank objects representing the bank accounts associated with the user.

    Raises:
    - HTTPException: If there is an internal server error while retrieving the bank accounts.

    """
    try:
        return account_controller.get_account_by_user(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
