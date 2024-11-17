import datetime
from pydantic import BaseModel
from fastapi import FastAPI

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str


repo = [
    Order(
        number=1,
        startDate=datetime.date(2000, 12, 1),  
        device="123",
        problemType="123",
        description="123",
        client="123",
        status="В ожидании"
    )
]

app = FastAPI()

@app.get("/")
def read_root():
    return repo

