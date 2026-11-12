# обновляем код в main.py
from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}


#То его вызов будет таким:

#'uvicorn main:my_awesome_api --reload'