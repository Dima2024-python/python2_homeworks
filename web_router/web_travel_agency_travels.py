from fastapi import APIRouter, Form, BackgroundTasks, HTTPException, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette import status
from fastapi.responses import RedirectResponse

import dao_travel_agency
from background_tasks_travel_agency.confirm_registration import confirm_registration
from dao_travel_agency import get_all_travel
from utils.jwt_auth import set_cookies_web, get_user_web
from utils.utils_hashlib import verify_password

templates = Jinja2Templates(directory="templates")


web_router = APIRouter(
    prefix=''
)


@web_router.get('/', include_in_schema=True)
@web_router.post('/', include_in_schema=True)
def index(request: Request, user=Depends(get_user_web)):
    print(999999999999999999)
    context = {
        'request': request,
        'travels': get_all_travel(25, 0),
        'navbar': 'default',
        'title': 'Main page',
        'user': user
    }
    response = templates.TemplateResponse('index.html', context=context)
    response_with_cookies = set_cookies_web(user, response)
    return response_with_cookies


@web_router.get('/search')
def search(request: Request):
    context = {
        'request': request,
        'travels': dao_travel_agency.get_all_travel(20, 0),
        'navbar': 'search',
        "title": 'Search'}
    return templates.TemplateResponse("index_search.html", context=context)


@web_router.get("/search_by_country", include_in_schema=True)
@web_router.post("/search_by_country", include_in_schema=True)
def search_by_country(request: Request, query: str = Form(None)):
    context = {
        "request": request,
        'navbar': 'search',
        "travels": dao_travel_agency.get_travel_by_country(query),
        "title": "Search",
    }
    response = templates.TemplateResponse("index_search.html", context=context)
    return response


@web_router.get("/get_all_travels", include_in_schema=True)
def get_all_travels(request: Request):
    context = {
        "request": request,
        'navbar': 'search',
        "travels": dao_travel_agency.get_all_travel(50, 0),
        "title": "Search",
    }
    response = templates.TemplateResponse("index_search.html", context=context)
    return response


@web_router.get("/search_by_price", include_in_schema=True)
@web_router.post("/search_by_price", include_in_schema=True)
def search_by_price(request: Request, query: float = Form(None)):
    context = {
        "request": request,
        'navbar': 'search',
        "travels": dao_travel_agency.get_travel_by_price(query),
        "title": "Search",
    }
    response = templates.TemplateResponse("index_search.html", context=context)
    return response


@web_router.get("/search_by_hotel_class", include_in_schema=True)
@web_router.post("/search_by_hotel_class", include_in_schema=True)
def search_by_hotel_class(request: Request, query: int = Form(None)):
    context = {
        "request": request,
        'navbar': 'search',
        "travels": dao_travel_agency.get_travel_by_hotel_class(query),
        "title": "Search",
    }
    response = templates.TemplateResponse("index_search.html", context=context)
    return response


@web_router.get('/register/', include_in_schema=True)
@web_router.post('/register/', include_in_schema=True)
def web_register(
        request: Request,
        background_tasks: BackgroundTasks,
        name: str = Form(None),
        email: str = Form(None),
        password: str = Form(None),
        user=Depends(get_user_web)
):
    if user:
        redirect_url = request.url_for('index')
        response = RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
        response_with_cookies = set_cookies_web(user, response)
        return response_with_cookies

    if request.method == 'GET':
        context = {
            'request': request,
            'navbar': 'default',
            'title': 'Register'
        }
        return templates.TemplateResponse('registration.html', context=context)

    maybe_user = dao_travel_agency.get_user_by_email(email)
    context = {
        'request': request,
        'title': 'Register',
        'navbar': 'default',
        'travels': get_all_travel(25, 0),
        'user': maybe_user
    }
    if not maybe_user:
        created_user = dao_travel_agency.create_user(name, email, password)
        background_tasks.add_task(confirm_registration, created_user, request.base_url)
        context['user'] = created_user

    # response = templates.TemplateResponse('index.html', context=context)
    redirect_url = request.url_for('index')
    response = RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    response_with_cookies = set_cookies_web(context['user'], response)
    return response_with_cookies


@web_router.get('/login/', include_in_schema=True)
@web_router.post('/login/', include_in_schema=True)
def web_login(
        request: Request,
        email: str = Form(None),
        password: str = Form(None),
        user=Depends(get_user_web)
):
    if user:
        redirect_url = request.url_for('index')
        response = RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
        response_with_cookies = set_cookies_web(user, response)
        return response_with_cookies

    if request.method == 'GET':
        context = {
            'request': request,
            'navbar': 'default',
            'title': 'Login'
        }
        return templates.TemplateResponse('login.html', context=context)

    maybe_user = dao_travel_agency.get_user_by_email(email)

    if not maybe_user:
        context = {
            'request': request,
            'title': 'Login',
            'error': True,
            'navbar': 'default',
            'email_value': email
        }
        return templates.TemplateResponse('login.html', context=context)

    if verify_password(password, maybe_user.hashed_password):
        context = {
            'request': request,
            'title': 'Register',
            'navbar': 'default',
            'travels': get_all_travel(25, 0),
            'user': maybe_user
        }
        response = templates.TemplateResponse('index.html', context=context)
        response_with_cookies = set_cookies_web(user, response)
        return response_with_cookies

    context = {
        'request': request,
        'title': 'Login',
        'navbar': 'default',
        'error': True,
        'email_value': email
    }
    return templates.TemplateResponse('login.html', context=context)


@web_router.get('/logout/', include_in_schema=True)
def web_logout(
        request: Request,
):
    context = {
        'request': request,
        'travels': get_all_travel(25, 0),
        'navbar': 'default',
        'title': 'Main page',
        'user': None
    }
    response = templates.TemplateResponse('index.html', context=context)
    response.delete_cookie('token_user_hillel')
    return response


@web_router.get("/travel/{travel_id}", include_in_schema=True)
def get_travel_by_id_web(request: Request, travel_id: int, user=Depends(get_user_web)):
    travel = dao_travel_agency.get_travel_by_id(travel_id)
    context = {
        "request": request,
        "travel": travel,
        'navbar': 'None',
        "title": "Details",
        "user": user,
    }
    response = templates.TemplateResponse("details.html", context=context)
    response_with_cookies = set_cookies_web(user, response)
    return response_with_cookies
