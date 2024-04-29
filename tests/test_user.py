import pytest
from fastapi.testclient import TestClient
from main import app
from models.user import User
from services.user_service import UserService

import sys

sys.path.append("..")
user_service = UserService()

client = TestClient(app)
created_users = []


@pytest.fixture(scope="module")
def test_client():
    yield client
    for user_id in created_users:
        user_service.delete_user(user_id)
    created_users.clear()


def test_create_user(test_client):
    new_user_data = {
        "id": "123123",
        "username": "test_user",
        "name": "Test User",
        "email": "test2@example.com",
        "phone": "1234"
    }
    response = test_client.post("/users", json=new_user_data)
    assert response.status_code == 200
    created_user = User(**response.json())
    created_users.append(created_user.id)
    assert created_user.username == new_user_data["username"]
    assert created_user.name == new_user_data["name"]
    assert created_user.email == new_user_data["email"]
    assert created_user.phone == new_user_data["phone"]
    assert created_user.created_at is not None
    assert created_user.updated_at is not None


def test_get_user(test_client):
    new_user_data = {
        "id": "123123",
        "username": "test_user",
        "name": "Test User",
        "email": "test3@example.com",
        "phone": "656446"
    }
    response = test_client.post("/users", json=new_user_data)
    assert response.status_code == 200
    created_user = User(**response.json())
    created_users.append(created_user.id)
    created_user_id = created_user.id

    response = test_client.get(f"/users/{created_user_id}")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == new_user_data["username"]
    assert user_data["name"] == new_user_data["name"]
    assert user_data["email"] == new_user_data["email"]
    assert user_data["phone"] == new_user_data["phone"]


def test_update_user(test_client):
    new_user_data = {
        "id": "asdasd",
        "username": "test_user_update",
        "name": "Test User Update",
        "email": "testupdate@example.com",
        "phone": "1234567890"
    }
    response = test_client.post("/users", json=new_user_data)
    assert response.status_code == 200
    created_user = User(**response.json())
    created_users.append(created_user.id)
    created_user_id = created_user.id

    # Actualizar los datos del usuario
    updated_user_data = {
        "id": created_user_id,
        "username": "updated_user",
        "name": "Updated User",
        "email": "updated@example.com",
        "phone": "0987654321"
    }
    response = test_client.put(
        f"/users/{created_user_id}", json=updated_user_data)
    assert response.status_code == 200
    updated_user = User(**response.json())
    assert updated_user.username == updated_user_data["username"]
    assert updated_user.name == updated_user_data["name"]
    assert updated_user.email == updated_user_data["email"]
    assert updated_user.phone == updated_user_data["phone"]


def test_delete_user(test_client):
    new_user_data = {
        "id": "asdasd",
        "username": "test_user_delete",
        "name": "Test User Delete",
        "email": "testdelete@example.com",
        "phone": "1234567890"
    }
    response = test_client.post("/users", json=new_user_data)
    assert response.status_code == 200
    created_user = User(**response.json())
    created_user_id = created_user.id

    response = test_client.delete(f"/users/{created_user_id}")
    assert response.status_code == 204

    response = test_client.get(f"/users/{created_user_id}")
    assert response.status_code == 404


def test_get_all_users(test_client):
    new_users_data = [
        {
            "id": "asdasd",
            "username": "user1",
            "name": "User One",
            "email": "user1@example.com",
            "phone": "1234567890"
        },
        {
            "id": "asdasd",
            "username": "user2",
            "name": "User Two",
            "email": "user2@example.com",
            "phone": "0987654321"
        }
    ]
    for user_data in new_users_data:
        response = test_client.post("/users", json=user_data)
        assert response.status_code == 200
        created_user = User(**response.json())
        created_users.append(created_user.id)

    response = client.get("/users")
    assert response.status_code == 200
    users_data = response.json()

    for user_data in new_users_data:
        assert user_data["username"] in [user["username"]
                                         for user in users_data]
        assert user_data["name"] in [user["name"] for user in users_data]
        assert user_data["email"] in [user["email"] for user in users_data]
        assert user_data["phone"] in [user["phone"] for user in users_data]
