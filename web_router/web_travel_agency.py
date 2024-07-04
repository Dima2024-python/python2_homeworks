from fastapi import APIRouter
from starlette.requests import Request

from travel_agency import templates


web_router = APIRouter(
    prefix=''
)


@app.get('/', include_in_schema=True)
def index_web(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'data': {}, 'title': 'Main page'})
