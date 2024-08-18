from datetime import datetime

from fastapi import Path, APIRouter, HTTPException
from pydantic import BaseModel, Field, HttpUrl
from starlette import status

import dao_travel_agency


api_router = APIRouter(prefix='/api', tags=['travel'])


class NewTravel(BaseModel):
    title: str = Field(max_length=100, min_length=2, examples=["Подорож до"])
    country: str = Field(default="France")
    description: str = Field(max_length=100, default="", examples=["Захоплююча подорож до"])
    price: float = Field(ge=0.01, examples=[100.78])
    hotel_class: int = Field(gt=0, le=5, default=4)
    image: HttpUrl
    date_start: datetime
    date_end: datetime


class TravelData(NewTravel):
    id: int


@api_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_travel(new_travel: NewTravel) -> NewTravel:
    travel = dao_travel_agency.create_travel(**new_travel.dict())
    return travel


@api_router.get("/get_all_travel")
def get_all_travel() -> list[NewTravel]:
    travels = dao_travel_agency.get_all_travel(50, 0)
    return travels


@api_router.get("/travel/{travel_id}")
def get_travel_by_id(travel_id: int) -> NewTravel:
    travel = dao_travel_agency.get_travel_by_id(travel_id)
    return travel


@api_router.get('/travel_by_country')
def get_travel_by_country(travel_country) -> list[NewTravel]:
    travel = dao_travel_agency.get_travel_by_country(travel_country)
    return travel


@api_router.put('/travel/{travel_id}')
def update_travel(updated_travel: NewTravel, travel_id: int = Path(gt=0, description='Id of the travel')) -> NewTravel:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    travel = dao_travel_agency.update_travel(travel_id, updated_travel.dict())
    return travel


@api_router.delete("/{travel_id}")
def delete_travel(
    travel_id: int = Path(gt=0, description="ID of the travel"),
) -> bool:
    travel = dao_travel_agency.get_travel_by_id(travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    dao_travel_agency.delete_travel(travel_id=travel_id)
    return True


