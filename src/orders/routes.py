from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.orders.order_data import orders
from typing import List
from src.orders.schemas import Order,OrderUpdateModel

order_router = APIRouter()

@order_router.get('/', response_model=List[Order])
async def get_all_orders():
    return orders

@order_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_order(order_data:Order)->dict:
    new_order = order_data.model_dump()
    orders.append(new_order)
    return new_order

@order_router.get('/{order_id}')
async def get_order(order_id:int)->dict:
    for order in orders:
        if order['id'] == order_id:
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@order_router.patch('/{order_id}')
async def update_order(order_id:int, order_update_data:OrderUpdateModel)->dict:
    for order in orders:
        if order['id'] == order_id:
            order['title'] = order_update_data.title
            order['unit_price'] = order_update_data.unit_price
            order['quantity'] = order_update_data.quantity
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

@order_router.delete('/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id:int):
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")    