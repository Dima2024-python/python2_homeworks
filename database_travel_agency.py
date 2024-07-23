from datetime import datetime

from sqlalchemy import Column, Float, Integer, Sequence, Text, create_engine, String, UUID, Boolean, ForeignKey, \
    DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

import uuid
import config

Base = declarative_base()


class MixInfoTravel:
    id = Column(Integer, Sequence("id"), primary_key=True)


class Travels(MixInfoTravel, Base):
    __tablename__ = "Travels"

    country = Column(Text, nullable=False)
    hotel_class = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    date_start = Column(Text, default="19:00, 08.09.2023", nullable=False)
    date_end = Column(Text, default="14:00, 28.09.2023", nullable=False)
    cover_url = Column(Text, nullable=False)
    ticket_quantity = Column(Integer, nullable=False)

    def __str__(self):
        return f"Travel: Country({self.country}), Hotel class({self.hotel_class}), Price({self.price}), Date({self.date_start})"

    __repr__ = __str__


class User(MixInfoTravel, Base):
    __tablename__ = 'Users'

    name = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    user_uuid = Column(UUID, default=uuid.uuid4)
    is_verified = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    def __str__(self):
        return f'<User name: {self.name}; Email: {self.email}>'

    __repr__ = __str__


class Order(MixInfoTravel, Base):
    __tablename__ = "User_orders"

    user_id = Column(ForeignKey('Users.id'), nullable=False)
    is_closed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f"Order: {self.id};  {self.user_id};  {self.is_closed}"

    __repr__ = __str__


class OrderTravels(MixInfoTravel, Base):
    __tablename__ = "Order_ravels"

    order_id = Column(ForeignKey('User_orders.id'), nullable=False)
    travel_id = Column(ForeignKey('Travels.id'), nullable=False)
    price = Column(Float, nullable=False)
    ticket_quantity = Column(Integer, nullable=False, default=0)

    @property
    def cost(self):
        return self.ticket_quantity * self.price

    def __str__(self):
        return f"Order_travel: {self.id}; {self.order_id};  {self.price}; Cost({self.cost})"

    __repr__ = __str__

engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
