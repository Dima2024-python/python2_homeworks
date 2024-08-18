import uuid

from sqlalchemy.orm import joinedload
from sqlalchemy import select

from database_travel_agency import Travel, session, User, OrderTravel
from utils.utils_hashlib import get_password_hash


def create_travel(
    title: str, description: str, price: float, country: str, image, hotel_class: int, date_start, date_end
) -> Travel:
    travel = Travel(
        title=title,
        country=country,
        description=description,
        price=price,
        hotel_class=hotel_class,
        image=str(image),
        date_start=date_start,
        date_end=date_end,
    )
    session.add(travel)
    session.commit()
    return travel


def get_all_travel(limit: int, skip: int, title: str | None = None) -> list[Travel]:
    if title:
        travels = session.query(Travel).filter(Travel.title.icontains(title)).limit(limit).offset(skip).all()
    else:
        travels = session.query(Travel).limit(limit).offset(skip).all()
    return travels


def get_travel_by_id(travel_id) -> Travel | None:
    travel = session.query(Travel).filter(Travel.id == travel_id).first()
    return travel


def delete_travel(travel_id) -> None:
    session.query(Travel).filter(Travel.id == travel_id).delete()
    session.commit()


def get_travel_by_country(travel_country) -> list[Travel]:
    travel = session.query(Travel).filter(Travel.country == travel_country).all()
    return travel


def get_travel_by_price(travel_price) -> list[Travel]:
    travel = session.query(Travel).filter(Travel.price == travel_price).all()
    print(travel, 999999999999999999999999999)
    return travel


def get_travel_by_hotel_class(travel_hotel_class) -> list[Travel]:
    travel = session.query(Travel).filter(Travel.hotel_class == travel_hotel_class).all()
    print(travel, 7777777777777777777777)
    return travel


def update_travel(travel_id: int, travel_data: dict) -> Travel:
    travel_data['image'] = str(travel_data['image'])
    session.query(Travel).filter(Travel.id == travel_id).update(travel_data)
    session.commit()
    travel = session.query(Travel).filter(Travel.id == travel_id).first()
    return travel


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
    user = session.query(User).filter(User.email == email).first()
    return user


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


def get_or_create(model, **kwargs):
    query = select(model).filter_by(**kwargs)
    instance = session.execute(query).scalar_one_or_none()
    if instance:
        return instance

    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance


def fetch_order_travels(order_id: int) -> list:
    query = select(OrderTravel).filter(
        OrderTravel.order_id == order_id
    ).options(joinedload(OrderTravel.travel))
    result = session.execute(query).scalars().all()
    return result
