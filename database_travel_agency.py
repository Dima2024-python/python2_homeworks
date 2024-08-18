from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, Sequence, Text, create_engine, String, UUID, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

import config

import uuid

Base = declarative_base()


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


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
