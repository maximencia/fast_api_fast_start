from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

api = FastAPI()

#Создайте приложение FastAPI, которое принимает POST-запрос к конечной точке (маршруту, адресу странички)
# `/calculate` с двумя числами (`num1` и `num2`) в качестве входных данных. Приложение должно ответить суммой двух чисел.
#Например, запрос на `/calculate` с `num1=5` и `num2=10` должен возвращать `{"result": 15}` в ответе.
#(Примечание: Вы можете использовать любой метод по вашему выбору для запуска приложения FastAPI для тестирования конечной точки).



class NumbersInput(BaseModel):
    num1: float
    num2: float


@api.post("/calculate")
def calculate_sum(data: NumbersInput):
    total = data.num1 + data.num2
    return {"result": int(total) if total.is_integer() else total}


#То его вызов будет таким:

#'uvicorn main:api --reload'
#uvicorn main:api --reload --port 8001

# C:\002_REPO\fast_api>curl -X POST "http://127.0.0.1:8002/calculate" -H "Content-Type: application/json" -d "{\"num1\": 5, \"num2\": 10}"
# {"result":15}