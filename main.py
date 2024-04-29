from fastapi import FastAPI
from routes.user import user
from routes.accountBank import accountBank

app = FastAPI(
    title="FastAPI MongoDB",
    description="This is a simple example of FastAPI with MongoDB",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "Operations related to users."
        },
        {
            "name": "Bank Account",
            "description": "Operations related to bank accounts."
        }
    ]
)

app.include_router(user)
app.include_router(accountBank)

