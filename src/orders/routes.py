from fastapi import APIRouter, status, Depends, Request
from fastapi.exceptions import HTTPException
from typing import List
from src.orders.service import OrderService
from src.orders.schemas import Order, OrderUpdateModel, OrderCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.dependencies import AccessTokenBearer

order_router = APIRouter()
order_service = OrderService()
access_token_bearer = AccessTokenBearer()

@order_router.get('/', response_model=List[Order])
async def get_all_orders(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print("User details:", user_details)
    orders = await order_service.get_all_orders(session)
    return orders

@order_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Order)
async def create_a_order(request: Request, order_data: OrderCreateModel, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print("Request body:", await request.body())  # Log raw request body
    print("Received order data:", order_data)  # Log parsed order data
    new_order = await order_service.create_order(order_data, session)
    return new_order

@order_router.get('/{order_uid}', response_model=Order)
async def get_order(order_uid: str, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    order = await order_service.get_order(order_uid, session)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@order_router.patch('/{order_uid}', response_model=Order)
async def update_order(request: Request, order_uid: str, order_update_data: OrderUpdateModel, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print("Request body:", await request.body())  # Log raw request body
    updated_order = await order_service.update_order(order_uid, order_update_data, session)
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return updated_order

@order_router.delete('/{order_uid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_uid: str, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    order_to_delete = await order_service.delete_order(order_uid, session)
    if order_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return {}
