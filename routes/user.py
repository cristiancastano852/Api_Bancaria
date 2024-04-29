from fastapi import APIRouter, Response, status, HTTPException
from controllers.user_controller import UserController
from services.user_service import UserService
from models.user import User
from typing import List

user = APIRouter()
user_service = UserService()
user_controller = UserController(user_service)


@user.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: str):
    """
    Get a user by their ID.

    Parameters:
    - user_id (str): The ID of the user to retrieve.

    Returns:
    - User: The user object.

    Raises:
    - HTTPException: If there is an HTTP error.
    - HTTPException: If there is an internal server error.

    """
    try:
        return user_controller.get_user(user_id)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@user.get("/users", response_model=List[User], tags=["Users"])
def get_all_users():
    """
    Get all users.

    Returns a list of all users.

    Returns:
        List[User]: A list of User objects representing all users.

    Raises:
        HTTPException: If there is an error retrieving the users.
    """
    return user_controller.get_all_users()


@user.post("/users", response_model=User, tags=["Users"])
def create_user(user: User):
    """
    Create a new user.

    Parameters:
    - user (User): The user object containing the user details.

    Returns:
    - User: The created user object.

    Raises:
    - HTTPException: If there is an error creating the user.

    """
    try:
        return user_controller.create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@user.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: str, user: User):
    """
    Update a user with the given user ID.

    Parameters:
    - user_id (str): The ID of the user to be updated.
    - user (User): The updated user object.

    Returns:
    - User: The updated user object.

    Raises:
    - HTTPException: If there is an error updating the user.

    """
    try:
        return user_controller.update_user(user_id, user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@user.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: str):
    """
    Delete a user by user ID.

    Parameters:
    - user_id (str): The ID of the user to be deleted.

    Raises:
    - HTTPException: If there is an error while deleting the user.

    """
    try:
        return user_controller.delete_user(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
