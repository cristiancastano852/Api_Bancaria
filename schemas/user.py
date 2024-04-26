def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username": item["username"],
        "name": item["name"],
        "email": item["email"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
