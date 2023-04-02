from fastapi import FastAPI
import os
import sys

# add path to module finder
sys.path.insert(0, os.getcwd() + "\\lib")

# import custom module
from ds import DataSource

# reset terminal
os.system("cls")

# init ds
ds = DataSource()

# intit app
app = FastAPI()
ds.say_this("hello aero")

# make entities dynamic
# build auth

# basic routing
# root
@app.get("/")
async def root():
    return {"message": "index"}


# sessions
@app.get("/sessions")
async def root():
    return {"message": "sessions"}


# users
@app.get("/users")
async def root():
    return {"message": "users"}


# accounts
@app.get("/accounts")
async def root():
    return {"message": "accounts"}
