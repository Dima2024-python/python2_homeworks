from fastapi import Query, Path, HTTPException, APIRouter
from starlette import status

import dao_travel_agency
from api_router.schemas_travel_agency import NewTravel, TravelId


api_router_travel_agency = APIRouter(
    prefix='/api/travels',
    tags=["API", "Travels"]
)


@api_router_travel_agency.post("/create/", status_code=status.HTTP_201_CREATED)
def create_travel(new_travel: NewTravel) -> NewTravel:
    created_travel = dao_travel_agency.create_travel(**new_travel.dict())
    return created_travel


@api_router_travel_agency.get("/")
def get_travels(
    limit: int = Query(default=5, gt=0, le=50, description="Number of travel"),
    skip: int = Query(default=0, ge=0, description="How many to skip"),
    country: str = Query(default="", description="Part of the travel country"),
) -> list[NewTravel]:
    travel = dao_travel_agency.get_all_travels(limit=limit, skip=skip, country=country)
    return travel


@api_router_travel_agency.get("/{travel_id}")
def get_travel(
    travel_id: int = Path(gt=0, description="ID of the travel"),
) -> NewTravel:
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if travel:
        return travel
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")


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
    travel = dao_travel_agency.get_travel_by_id(travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    dao_travel_agency.delete_travel(travel_id=travel_id)
    return True


