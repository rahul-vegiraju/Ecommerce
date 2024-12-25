from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import date


class Order(SQLModel, table = True):
    __tablename__ = "orders"

    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    title: str
    unit_price: float
    quantity: int
    published_date: date
    created_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<ORDER {self.title}>"