import sys
import os
sys.path.insert(0, os.getcwd() + "\\lib")
from fastapi import FastAPI
from ds import DataSource
from routes import Routes


class Aero:
    app: FastAPI

    def __init__(self) -> None:
        # clear console
        os.system("cls")

        # init ds
        self.ds = DataSource()

        # intit app
        self.app = FastAPI()

        Routes(self.app)
