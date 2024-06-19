from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

books = [
    {
        'title': "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian, Political Fiction",
        'info': 'https://uk.wikipedia.org/wiki/1984_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)'

    },
    {
        'title': "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Southern Gothic, Bildungsroman",
        'info': 'https://uk.wikipedia.org/wiki/1984_(%D1%80%D0%BE%D0%BC%D0%B0%D0%BD)'
    },
    {
        'title': "The Great Gatsby",
        "author": 'F. Scott Fitzgerald',
        "year": 1925,
        "genre": "Tragedy",
        'info': 'https://uk.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%93%D0%B5%D1%82%D1%81%D0%B1%D1%96'
    },
    {
        'title': "Moby-Dick",
        "author": "Herman Melville",
        "year": 1851,
        "genre": "Adventure, Epic",
        'info': 'https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B1%D0%B8_%D0%94%D0%B8%D0%BA'
    },
    {
        'title': "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genre": "Romantic Fiction",
        'info': 'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%B4%D1%96%D1%81%D1%82%D1%8C_%D1%96_%D1%83%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F_(%D1%84%D1%96%D0%BB%D1%8C%D0%BC,_2005)'
    }
]


@app.get('/api/')
def index() -> dict:
    return {'status': 'OK'}


@app.get('/')
def index_(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'data': books, 'title': 'Main page'})

















































