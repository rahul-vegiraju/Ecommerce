from pydantic import BaseModel
class Order(BaseModel):
    id: int
    title: str
    unit_price: float
    quantity: int
    published_date:str

class OrderUpdateModel(BaseModel):
    title: str
    unit_price: float
    quantity: int
