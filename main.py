from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/book')
def create_book(item: Book):
    return item

'''
 1. Три точки - обязательный параметр
 2. min_l, max_l - длина параметра
 3. description - описание 
 4. Первый аргумент - значение по умолчанию
'''


@app.get('/book')
def get_book(parameter: str = Query("default", min_length=2, max_length=5, description="Parameter description")):
    return parameter


@app.get("/{name}")
async def say_hello(name: str, surname: str = None):
    response = {"message": f"Hello {name}"}
    if surname:
        response = {"message": f"Hello {name} {surname}"}
    return response
