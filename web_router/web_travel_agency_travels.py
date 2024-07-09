from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


web_router = APIRouter(
    prefix=''
)


@web_router.get('/', include_in_schema=True)
def index_web(request: Request) -> dict:
    context = {'request': request,
               'data': {},
               'title': 'Main page'}
    return templates.TemplateResponse('index.html', context=context)