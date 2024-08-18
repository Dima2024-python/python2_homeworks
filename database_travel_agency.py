from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, Sequence, Text, create_engine, String, UUID, Boolean, \
    ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

import config

import uuid

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    user_uuid = Column(UUID, default=uuid.uuid4)
    is_verified = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(ForeignKey('Users.id'), nullable=False)
    is_closed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f'<Order: {self.id=}; {self.user_id=}; {self.is_closed=}>'

    __repr__ = __str__


class OrderTravel(Base):
    __tablename__ = 'order_travels'

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    travel_id = Column(ForeignKey('Travels.id'), nullable=False)
    price = Column(Float, nullable=False, default=10.0)
    quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    travel = relationship('Travel', back_populates='travels')

    @property
    def cost(self):
        return self.quantity * self.price

    def __str__(self):
        return f'<OrderProduct: {self.id=}; {self.order_id=}; {self.quantity=}; {self.price=}, cost={self.cost}>'

    __repr__ = __str__


class Travel(Base):
    __tablename__ = "Travels"

    id = Column(Integer, Sequence("travel_id_seq"), primary_key=True)
    country = Column(String, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False, default=100.0)
    hotel_class = Column(Integer, nullable=False)
    image = Column(String, default="")
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    travels = relationship('OrderTravel', back_populates='travel')


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
