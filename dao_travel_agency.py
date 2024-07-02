from database_travel_agency import Travels, session


def create_travel(country: str, hotel_class: float, price: float, date_start: str, date_end: str) -> Travels:
    travel = Travels(country=country, hotel_class=hotel_class, price=price, date_start=date_start, date_end=date_end)
    session.add(travel)
    session.commit()
    return travel


def get_all_travels(limit: int, skip: int, country: str) -> list[Travels]:
    if country:
        travel = session.query(Travels).filter(Travels.country.icontains(country)).limit(limit).offset(skip).all()
    else:
        travel = session.query(Travels).limit(limit).offset(skip).all()
    return travel


def get_travel_by_id(travel_id) -> Travels | None:
    travel = session.query(Travels).filter(Travels.id == travel_id).first()
    return travel


def update_travel(travel_id: int, travel_data: dict) -> Travels:
    session.query(Travels).filter(Travels.id == travel_id).update(travel_data)
    session.commit()
    travel = session.query(Travels).filter(Travels.id == travel_id).first()
    return travel


def delete_travel(travel_id: int) -> None:
    session.query(Travels).filter(Travels.id == travel_id).delete()
    session.commit()
