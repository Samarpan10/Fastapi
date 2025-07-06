from fastapi import FastAPI

myapi = FastAPI()

@myapi.get("/")

def func():
    return {"message":"HelloWorld"}
