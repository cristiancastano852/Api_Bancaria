def accountEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user_id": item["user_id"],
        "account_number": item["account_number"],
        "balance": item["balance"],
        "account_type": item["account_type"],
        "is_active": item["is_active"],
        "created_at": item["created_at"].isoformat(),
        "updated_at": item["updated_at"].isoformat()
    }

def accountsEntity(entity) -> list:
    return [accountEntity(item) for item in entity]
