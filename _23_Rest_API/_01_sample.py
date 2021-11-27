from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def msg():
    return "hello world"


"""@app.get("/")
async def root():
    return {"message": "Hello World"} """
