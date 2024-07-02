from fastapi import FastAPI, Query, Path, HTTPException
from fastapi.templating import Jinja2Templates
from starlette import status

import config
import dao_travel_agency
from database_travel_agency import create_tables
from schemas import NewTravel, TravelId, DeletedTravel

templates = Jinja2Templates(directory='templates')

def lifespan(app: FastAPI):
    create_tables()
    yield



app = FastAPI(
    debug=config.DEBUG,
    lifespan=lifespan,
)


@app.post('/api/travels/create/', status_code=status.HTTP_201_CREATED, tags=['API', 'Products'])
def create_travel(new_travel: NewTravel) -> NewTravel:
    created_travel = dao_travel_agency.create_travel(**new_travel.dict())
    return created_travel


@app.get('/api/travels/', tags=['API', 'Travels'])
def get_travels(
        limit: int = Query(default=5, gt=0, le=50, description='Number of travel'),
        skip: int = Query(default=0, ge=0, description='How many to skip'),
        country: str = Query(default='', description='Part of the travel country'),
) -> list[NewTravel]:
    travel = dao_travel_agency.get_all_travels(limit=limit, skip=skip, country=country)
    return travel


@app.get('/api/travels/{travel_id}', tags=['API', 'Travels'])
def get_travel(
        travel_id: int = Path(gt=0, description='ID of the travel'),
) -> NewTravel:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if travel:
        return travel
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')


@app.put('/api/travels/{travel_id}', tags=['API', 'Travels'])
def update_travel(
        updated_travel: NewTravel,
        travel_id: int = Path(gt=0, description='ID of the travel'),
) -> TravelId:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')

    travel = dao_travel_agency.update_travel(travel_id, updated_travel.dict())
    return travel


@app.delete('/api/travels/{travel_id}', tags=['API', 'Travels'])
def delete_travel(
        travel_id: int = Path(gt=0, description='ID of the travel'),
) -> DeletedTravel:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    dao_travel_agency.delete_travel(travel_id=travel_id)
    return DeletedTravel(id=TravelId)