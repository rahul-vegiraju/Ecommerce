from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
import uuid
from datetime import datetime

class User(SQLModel, table=True):  # Use SQLModel as the base class and include `table=True`
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        sa_column_kwargs={"nullable": False}
    )
    username: str = Field(nullable=False, unique=True)
    email: str = Field(nullable=False, unique=True)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    is_verified: bool = Field(default=False)
    password_hash: str = Field(nullable=False, exclude=True)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"nullable": False, "default": datetime.utcnow},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"nullable": False, "default": datetime.utcnow, "onupdate": datetime.utcnow},
    )

    def __repr__(self):
        return f"<User {self.username}>"
