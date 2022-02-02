from pydantic import BaseModel, Field, validator
from typing import List
import datetime


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    name: str = Field(..., max_length=30, )
    age: int = Field(..., gt=15, lt=90, description="Authors age")

    # @validator('age')
    # def validate_age(cls, value):
    #     if value < 15:
    #         raise ValueError('Author age must be more than 15')
    #     elif value > 90:
    #         raise ValueError('Author age must be less than 90')
    #     return value


class Book(BaseModel):
    title: str
    description: str
    date: datetime.datetime = Field(datetime.datetime.now(), )  # Указание типа времени
    # genres: str = None  # None по умолчанию
    genres: List[Genre] = []  # Many to Many
    pages: int = 20
