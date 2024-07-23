import uuid

from database_travel_agency import Travels, User, session
from utils.utils_hashlib import get_password_hash


def create_travel(country: str, hotel_class: float, price: float, date_start: str, date_end: str, cover_url, ticket_quantity: int) -> Travels:
    travel = Travels(country=country,
                     hotel_class=hotel_class,
                     price=price, date_start=date_start,
                     date_end=date_end,
                     cover_url=str(cover_url),
                     ticket_quantity=ticket_quantity)
    session.add(travel)
    session.commit()
    return travel


def get_all_travels(limit: int, skip: int) -> list[Travels]:
    travels = session.query(Travels).filter(Travels.ticket_quantity > 0).limit(limit).offset(skip).all()
    return travels


def get_travels_by_hotel_class_and_price(hotel_class, price) -> list[Travels]:
    travels = session.query(Travels).filter(Travels.price == price, Travels.hotel_class == hotel_class)
    return travels


def get_travels_by_price(price) -> list[Travels]:
    travels = session.query(Travels).filter(Travels.price == price)
    return travels


def get_travel_by_country(country) -> list[Travels]:
    travels = session.query(Travels).filter(Travels.country == country)
    return travels


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


def create_user(name: str, email: str, password: str) -> User:
    try:
        user = User(
            name=name,
            email=email,
            hashed_password=get_password_hash(password),
        )
        session.add(user)
        session.commit()
        return user
    except Exception:
        return session.rollback()


def get_user_by_email(email: str) -> User | None:
    query = session.query(User).filter(User.email == email).first()
    return query


def get_user_by_uuid(user_uuid: uuid.UUID | str) -> User | None:
    query = session.query(User).filter(User.user_uuid == user_uuid).first()
    return query


def activate_account(user: User) -> User:
    if user.is_verified:
        return user
    
    user.is_verified = True
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
