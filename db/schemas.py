import uuid
from datetime import time
from typing import List, Optional

from pydantic import BaseModel


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class StreetBase(BaseModel):
    name: str
    city: uuid.UUID


class StreetCreate(StreetBase):
    pass


class ShopBase(BaseModel):
    title: str
    open_time: time
    close_time: time


class ShopCreate(StreetBase):
    pass


class Shop(ShopBase):
    id: uuid.UUID
    city: uuid.UUID
    street: uuid.UUID


class Street(StreetBase):
    id: uuid.UUID
    city: uuid.UUID
    shops = List[Shop] = []

    class Config:
        orm_mode = True


class City(CityBase):
    id: uuid.UUID
    streets: List[Street] = []
    shops = List[Shop] = []

    class Config:
        orm_mode = True
