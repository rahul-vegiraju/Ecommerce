from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import OrderCreateModel, OrderUpdateModel
from sqlmodel import select, desc
from .models import Order
from datetime import date
from datetime import datetime

class OrderService:
    async def get_all_orders(self, session:AsyncSession):
        statement = select(Order).order_by(desc(Order.created_at))

        result = await session.exec(statement)

        return result.all()
    
   
    async def get_order(self, order_uid:str,session:AsyncSession):
        statement = select(Order).where(Order.uid == order_uid)

        result = await session.exec(statement)

        order = result.first()

        return order if order is not None else None
   

    async def create_order(self, order_data: OrderCreateModel ,session:AsyncSession):
        order_data_dict = order_data.model_dump()

        new_order = Order(
            **order_data_dict
        )

        new_order.published_date = datetime.strptime(order_data_dict['published_date'], "%Y-%m-%d")
        session.add(new_order)

        await session.commit()

        return new_order


    async def update_order(self, order_uid:str,update_data: OrderUpdateModel, session: AsyncSession):
        order_to_update = await self.get_order(order_uid, session)

        if order_to_update is not None:
            update_data_dict = update_data.model_dump()

            for i,j in update_data_dict.items():
                setattr(order_to_update, i, j)
        
            await session.commit()

            return order_to_update
        else:
            return None
    
    async def delete_order(self, order_uid:str, session:AsyncSession):
        order_to_delete = await self.get_order(order_uid, session)

        if order_to_delete is not None:
            await session.delete(order_to_delete)

            await session.commit()

            return {}
        
        else:
            return None