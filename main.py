from fastapi import FastAPI
import os
import sys


# import from dir is too complex
cwd = os.getcwd()

# Insert the path of modules folder
sys.path.insert(0, cwd + "\\ds")

# get data source from aero
from aero import DataSource

# reset terminal
os.system("cls")

# init ds
ds = DataSource()

# intit app
app = FastAPI()
ds.say_this("hello aero")

# create Entities for auth
# include auth


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
