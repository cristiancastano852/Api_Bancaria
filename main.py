from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="FastAPI MongoDB",
    description="This is a simple example of FastAPI with MongoDB",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations related to users."
        }
    ]
)

app.include_router(user)

