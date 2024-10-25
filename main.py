from fastapi import FastAPI
from models import RequestData, ResponseData
from utils import place_order_util

app = FastAPI()

@app.post("/place_order", response_model=ResponseData)
def place_order(request_data: RequestData):
    return place_order_util(request_data)
