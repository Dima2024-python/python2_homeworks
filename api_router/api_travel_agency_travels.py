from fastapi import Path, HTTPException, APIRouter
from starlette import status

import dao_travel_agency
from schemas_travel_agency_travels import NewTravel, TravelId


api_router_travel_agency = APIRouter(
    prefix='/api/travels',
    tags=["API Travels"]
)


@api_router_travel_agency.post("/create/", status_code=status.HTTP_201_CREATED)
def create_travel(new_travel: NewTravel) -> NewTravel:
    created_travel = dao_travel_agency.create_travel(**new_travel.dict())
    return created_travel


@api_router_travel_agency.get("/")
def get_all_travels() -> list[NewTravel]:
    travels = dao_travel_agency.get_all_travels()
    return travels


@api_router_travel_agency.get("/travels_by_price")
def get_travels_by_price(price) -> list[NewTravel]:
    travels = dao_travel_agency.get_travels_by_price(price=price)
    return travels


@api_router_travel_agency.get("/travels_by_country")
def get_travels_by_country(country) -> list[NewTravel]:
    travels = dao_travel_agency.get_travel_by_country(country=country)
    return travels


@api_router_travel_agency.get("/{travel_hotel_class_and_price}")
def get_travels_by_hotel_class_and_price(price, hotel_class) -> list[NewTravel]:
    travel = dao_travel_agency.get_travels_by_hotel_class_and_price(price=price, hotel_class=hotel_class)
    return travel


@api_router_travel_agency.put("/{travel_id}")
def update_travel(
    updated_travel: NewTravel,
    travel_id: int = Path(gt=0, description="ID of the travel"),
) -> TravelId:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    travel = dao_travel_agency.update_travel(travel_id, updated_travel.dict())
    return travel


@api_router_travel_agency.delete("/{travel_id}")
def delete_travel(
    travel_id: int = Path(gt=0, description="ID of the travel"),
) -> bool:
    travel = dao_travel_agency.get_travel_by_id()
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    dao_travel_agency.delete_travel(travel_id=travel_id)
    return True


