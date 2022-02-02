from pydantic import BaseModel
from typing import List
import datetime


class Genre(BaseModel):
    id: int
    name: str


class Book(BaseModel):
    id: int
    title: str
    description: str
    date: datetime.datetime  # Указание типа времени
    # genres: str = None  # None по умолчанию
    genres: List[Genre]  # Many to Many
    pages: int = 20
