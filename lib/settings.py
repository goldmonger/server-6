from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "aero-demo"
    host: str = ""
    port: str = ""

    class Config:
        env_file = ".env"
