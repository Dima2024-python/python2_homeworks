from fastapi import FastAPI

import config
from api_router.api_travel_agency_travels import api_router
from api_router.api_travel_agency_users import api_router_travel_agency_users
from database_travel_agency import create_tables
from web_router.web_travel_agency_travels import web_router


def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    debug=config.DEBUG,
    lifespan=lifespan,
)


app.include_router(api_router)
app.include_router(web_router)
app.include_router(api_router_travel_agency_users)
