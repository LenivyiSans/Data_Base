"""from-откуда, import-что переносим сюда"""
from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

"""ЭТО Объект"""

app = FastAPI()

"""Это Класс!!!"""


class Post(BaseModel):
    id: int
    title: str
    body: str


"""Это Объект"""
posts = [
    {'id': 1, 'title': 'New 1', 'body': 'Text 1'},
    {'id': 2, 'title': 'New 2', 'body': 'Text 2'},
    {'id': 3, 'title': 'New 3', 'body': 'Text 3'},
    {'id': 4, 'title': 'New 4', 'body': 'Text 4'},
]

"""Это просто более сложный вариант items НЕТ никаких плюсов, если что это URL-страницы !!!"""
# @app.get("/items")
# async def items() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'], title=post['title'], body=post['body']))
#     return post_objects


"""Это более легкий вариант items по сути, он тупо лучше(быстрее и легкче написать) чем верхний вариант """


@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post

    raise HTTPException(status_code=404, detail='Post ne naiden')


@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404, detail='Post ne существует')
    else:
        return {"data": "figniy post ne naiden"}
