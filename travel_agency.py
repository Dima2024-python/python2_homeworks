from fastapi import Request

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import config
from api_router.api_travel_agenci import api_router_travel_agency
from database_travel_agency import create_tables
from web_router.web_travel_agency import web_router

templates = Jinja2Templates(directory="templates")


def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    debug=config.DEBUG,
    lifespan=lifespan,
)


app.include_router(api_router_travel_agency)
app.include_router(web_router)
