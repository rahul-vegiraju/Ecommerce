from pydantic import BaseModel
import uuid
from datetime import datetime
from datetime import date

class Order(BaseModel):
    uid: uuid.UUID
    title: str
    unit_price: float
    quantity: int
    published_date: date
    created_at: datetime
    update_at: datetime

class OrderCreateModel(BaseModel):
    title: str
    unit_price: float
    quantity: int
    published_date:str

    
class OrderUpdateModel(BaseModel):
    title: str
    unit_price: float
    quantity: int
