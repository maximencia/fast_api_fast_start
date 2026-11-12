from fastapi import FastAPI
from fastapi.responses import FileResponse

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
def root():
    return FileResponse("index.html")


# альтернативный вариант
@my_awesome_api.get("/file", response_class=FileResponse)
def root_html():
    return "/index.html"


#То его вызов будет таким:

#'uvicorn main:my_awesome_api --reload'
#uvicorn main:my_awesome_api --reload --port 8001