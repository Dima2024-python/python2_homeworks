from datetime import datetime

from sqlalchemy import Column, Integer, Sequence, String, Text, Float, DateTime, create_engine, UUID, Boolean, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base, relationship

import uuid
import config

Base = declarative_base()


class MixInfoTravel:
    id = Column(Integer, Sequence("id"), primary_key=True)
