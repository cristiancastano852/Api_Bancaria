import pytest
from fastapi.testclient import TestClient
from main import app

from models.accountBank import AccountBank
from services.accountBank_service import AccountBankService
from controllers.accountBank_controller import AccountBankController

client = TestClient(app)

account_service = AccountBankService()
account_controller = AccountBankController(account_service)


def test_create_account():
    # create a new account with valid data
    valid_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=valid_account_data)

    assert response.status_code == 200

    created_account_data = response.json()
    assert "id" in created_account_data

    # delete the created account
    account_service.delete_account(created_account_data["id"])

    # check if the user_id is a valid ObjectId
    invalid_account_data = {
        "id": "123123",
        "user_id": "invalid_user_id",  # invalid user_id
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }

    response = client.post("/accounts", json=invalid_account_data)
    assert response.status_code == 404

    # create a new account with invalid user_id
    invalid_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1992",  # user_id not found
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }

    response = client.post("/accounts", json=invalid_account_data)
    assert response.status_code == 404
    assert response.json() == {
        "detail": "User with id <662ee1c28c59e5cee83d1992> no found"}

    # create a new account with account_type not in AccountType
    invalid_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",  # invalid user_id
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "invalid_account_type",  # invalid account_type
        "is_active": True
    }

    response = client.post("/accounts", json=invalid_account_data)
    assert response.status_code == 422

    # create a new account without fields
    invalid_account_data = {
        "account_number": "123456789",
        "balance": 1000.0,
        "is_active": True
    }
    response = client.post("/accounts", json=invalid_account_data)
    assert response.status_code == 422


def test_get_account():
    # create a new account
    new_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=new_account_data)
    created_account_data = response.json()
    assert response.status_code == 200
    id_account = created_account_data["id"]

    # get the created account
    response = client.get(f"/accounts/{id_account}")
    assert response.status_code == 200

    account_data = response.json()
    assert account_data["user_id"] == new_account_data["user_id"]
    assert account_data["account_number"] == new_account_data["account_number"]
    assert account_data["balance"] == new_account_data["balance"]
    assert account_data["account_type"] == new_account_data["account_type"]
    assert account_data["is_active"] == new_account_data["is_active"]

    # delete the created account
    account_service.delete_account(id_account)

    # get an account that does not exist
    response = client.get("/accounts/invalid_account_id")
    assert response.status_code == 404


def test_get_all_accounts():
    # get all accounts
    response = client.get("/accounts")
    assert response.status_code == 200

    accounts_data = response.json()
    assert isinstance(accounts_data, list)


def test_update_balance():
    # create a new account
    new_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=new_account_data)
    assert response.status_code == 200
    created_account_data = response.json()
    id_account = created_account_data["id"]
    # update the balance of the created account with a positive amount (increase the balance)
    new_amount_positive = 500.0
    response = client.patch(
        f"/accounts/{id_account}?amount={new_amount_positive}")
    assert response.status_code == 200
    updated_account_data = response.json()
    assert updated_account_data["Saldo actualizado"]["balance"] == new_account_data["balance"] + new_amount_positive

    # update the balance of the created account with a negative amount (decrease the balance)
    new_amount_negative = -200.0
    response = client.patch(
        f"/accounts/{id_account}?amount={new_amount_negative}")
    assert response.status_code == 200

    # delete the created account
    account_service.delete_account(id_account)

    # update the balance of an account that does not exist
    response = client.patch(
        f"/accounts/662ee1c28c59e5cee83d1992?amount={new_amount_negative}")
    assert response.status_code == 404

    # update the balance of an account with an invalid format
    response = client.patch(
        f"/accounts/id_invalid_format?amount={new_amount_negative}")
    assert response.status_code == 500


def test_replace_balance():
    # create a new account
    new_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=new_account_data)
    assert response.status_code == 200
    created_account_data = response.json()
    id_account = created_account_data["id"]

    # replace the balance of the created account
    new_balance = 500.0
    response = client.put(f"/accounts/{id_account}?balance={new_balance}")
    assert response.status_code == 200
    updated_account_data = response.json()
    assert updated_account_data["balance"] == new_balance

    # delete the created account
    account_service.delete_account(id_account)

    # replace the balance of an account that does not exist
    response = client.put(
        f"/accounts/662ee1c28c59e5cee83d1992?balance={new_balance}")
    assert response.status_code == 500

    # replace the balance of an account with an invalid format
    response = client.put(f"/accounts/id_invalid_format?balance={new_balance}")
    assert response.status_code == 500


def test_delete_account():
    # create a new account
    new_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=new_account_data)
    assert response.status_code == 200
    created_account_data = response.json()
    id_account = created_account_data["id"]

    # delete the created account
    response = client.delete(f"/accounts/{id_account}")
    assert response.status_code == 204

    # delete an account that does not exist
    response = client.delete(f"/accounts/662ee1c28c59e5cee83d1992")
    assert response.status_code == 404

    # delete an account with an invalid format
    response = client.delete(f"/accounts/id_invalid_format")
    assert response.status_code == 500


def test_get_account_by_user_id():
    # create a new account
    new_account_data = {
        "id": "123123",
        "user_id": "662ee1c28c59e5cee83d1994",
        "account_number": "123456789",
        "balance": 1000.0,
        "account_type": "Ahorros",
        "is_active": True
    }
    response = client.post("/accounts", json=new_account_data)
    assert response.status_code == 200
    created_account_data = response.json()
    id_account = created_account_data["id"]

    # get the created account by user_id
    response = client.get(f"/accounts/user/{new_account_data['user_id']}")
    assert response.status_code == 200

    account_data = response.json()
    assert account_data[0]["user_id"] == new_account_data["user_id"]
    assert account_data[0]["account_number"] == new_account_data["account_number"]
    assert account_data[0]["balance"] == new_account_data["balance"]
    assert account_data[0]["account_type"] == new_account_data["account_type"]
    assert account_data[0]["is_active"] == new_account_data["is_active"]

    # delete the created account
    account_service.delete_account(id_account)

    # get an account by user_id that does not exist
    response = client.get("/accounts/user/662ee1c28c59e5cee83d1992")
    assert response.status_code == 404
