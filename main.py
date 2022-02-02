from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


'''
 1. Три точки - обязательный параметр
 2. min_length=2, max_length=5 - длина параметра
 3. description - описание 
 4. Первый аргумент - значение по умолчанию
 5. List[str] - список параметров  с одним именем
 6. deprecated - Устаревший параметр
 7. gt - Наименьшее значение для int
 8. le - Наибольшее значение для int
 9. Path - для переменных в URL
 10. Query - для параметров
 11. Body - для добавления параметра в тело POST запроса
 12. response_model_exclude_unset=True - убирает ненужные данные с поля ответа
 13. response_model_exclude={"pages", "date"} - убирает указанные поля с ответа
'''


@app.get("/{name}")
async def say_hello(name: str, surname: str = None):
    response = {"message": f"Hello {name}"}
    if surname:
        response = {"message": f"Hello {name} {surname}"}
    return response


""" List """


@app.get('/books')
def books_view(parameter: str = Query(...,
                                      min_length=3,
                                      max_length=10,
                                      deprecated=True),
               parameter_list: List[str] = Query(["default", "2"],
                                                 description="Parameter description"),):
    return parameter, parameter_list


""" Retrieve """


@app.get('/books/{pk}')
def book_detail_view(pk: int = Path(..., gt=0, le=20),
                     pages: int = Query(None, gt=0, le=500)):
    return {"slug": pk,
            "pages": pages}

""" Create """


@app.post('/books',)
def create_book(item: Book = Body(..., embed=True)):

    return {"item": item}


@app.post('/author', response_model=Author)
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}
