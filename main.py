from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/api/')
def index() -> dict:
    return {'status': 'OK'}


@app.get('/')
def index_(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'data': 90909090, 'title': 'Main page'})

















































