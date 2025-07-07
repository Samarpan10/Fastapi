from fastapi import FastAPI

app = FastAPI()


@app.get("/samarpan")
def print_goru():
    return {"message":"goru"}


@app.get("/helloworld")
def print_hello():
    return {"message":"HelloWorld"}
