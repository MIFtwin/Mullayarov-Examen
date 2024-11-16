from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel

class Order(BaseModel):
    number: int
    startDate: date
    device: str
    problemType: str
    description: str
    client: str
    status: str

repo: List[Order] = [
    Order(
        number=1,
        startDate=date(2000, 12, 1),
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="В ожидании"
    )
]

app = FastAPI()

# Новый маршрут для корня
@app.get("/")
def read_root():
    return repo  # Возвращаем содержимое репозитория

# Существующий маршрут для получения всех заказов
@app.get("/orders")
def get_orders():
    return repo

# Маршрут для добавления нового заказа
@app.post("/orders")
def create_order(order: Order):
    repo.append(order)
    return {"message": "Order created successfully", "order": order}


