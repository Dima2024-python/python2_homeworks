from sqlalchemy import Column, Float, Integer, Sequence, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import config

Base = declarative_base()


class Travels(Base):
    __tablename__ = "Travel agency"

    id = Column(Integer, Sequence("Id of your travel"), primary_key=True)
    country = Column(Text, nullable=False)
    hotel_class = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    date_start = Column(Text, default="19:00, 08.09.2023", nullable=False)
    date_end = Column(Text, default="14:00, 28.09.2023", nullable=False)

    def __str__(self):
        return (
            f"Travel: Country({self.country}), Hotel class({self.hotel_class}), Price({self.price}), Date({self.date})"
        )

    __repr__ = __str__


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
