from datetime import datetime

from sqlalchemy import DateTime, Column, Float, Integer, Sequence, Text, create_engine, String, UUID, Boolean
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

    def __str__(self):
        return (
            f"Travel: Country({self.country}), Hotel class({self.hotel_class}), Price({self.price}), Date({self.date})"
        )

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


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
