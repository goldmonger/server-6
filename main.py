from fastapi import FastAPI
import os
import sqlalchemy


os.system("cls")
# print("sql alchemy version:", sqlalchemy.__version__)
# ds_engine = sqlalchemy.create_engine("mysql+mysqlconnector://server:donut@localhost:25060/7s", echo=True)
ds_engine = sqlalchemy.create_engine("mysql+mysqlconnector://server:donut@localhost:25060/7s")

app = FastAPI()


# include mysql ds

# create Entities for auth

# include auth

with ds_engine.connect() as ds:
    result = ds.execute(sqlalchemy.text("select 'hello world'"))
    print()


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