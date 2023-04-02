from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional

# base class for storing meta data for dynamic creation of entities
class Entity(DeclarativeBase):
    pass

# an example mapping using the base
class User(Entity):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[Optional[str]] = mapped_column(String(30))
