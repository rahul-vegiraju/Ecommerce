from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
from src.orders.service import OrderService
from src.orders.schemas import Order,OrderUpdateModel, OrderCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session

order_router = APIRouter()
order_service = OrderService()

@order_router.get('/', response_model=List[Order])
async def get_all_orders(session: AsyncSession = Depends(get_session)):
    orders = await order_service.get_all_orders(session)
    return orders

@order_router.post('/', status_code=status.HTTP_201_CREATED, response_model = Order)
async def create_a_order(order_data:OrderCreateModel, session: AsyncSession = Depends(get_session))->dict:
    new_order = await order_service.create_order(order_data, session)
    return new_order

@order_router.get('/{order_uid}', response_model =  Order)
async def get_order(order_uid:str, session:AsyncSession = Depends(get_session))->dict:
    order = await order_service.get_order(order_uid, session)

    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return order


@order_router.patch('/{order_uid}', response_model = Order)
async def update_order(order_uid:str, order_update_data:OrderUpdateModel, session:AsyncSession = Depends(get_session))->dict:
    updated_order = await order_service.update_order(order_uid, order_update_data, session)

    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    else:
        return updated_order
        


@order_router.delete('/{order_uid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_uid:str, session:AsyncSession = Depends(get_session)):
    order_to_delete = await order_service.delete_order(order_uid, session)

    if order_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    else:
        return {}