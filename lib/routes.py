from typing import Annotated
from fastapi import Depends
from actions import get_settings
from settings import Settings
from fastapi import FastAPI


class Routes:
    app: FastAPI

    def __init__(self, app: any) -> None:
        self.app = app

        # basic routing
        # root
        @self.app.get("/")
        async def root():
            return {"message": "index"}

        # root
        @self.app.get("/info")
        async def info(settings: Annotated[Settings, Depends(get_settings)]):
            return {
                "app_name": settings.app_name,
                "port": settings.port,
                "host": settings.host,
            }

        # sessions
        @self.app.get("/sessions")
        async def root():
            return {"message": "sessions"}

        # users
        @self.app.get("/users")
        async def root():
            return {"message": "users"}

        # accounts
        @self.app.get("/accounts")
        async def root():
            return {"message": "accounts"}
