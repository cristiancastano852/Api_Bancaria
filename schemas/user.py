def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username": item["username"],
        "name": item["name"],
        "email": item["email"],
        "phone": item["phone"],
        "created_at": item.get("created_at", None),
        "updated_at": item.get("updated_at", None),
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
