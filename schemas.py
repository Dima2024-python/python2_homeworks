from datetime import datetime
from pydantic import BaseModel, Field


class NewTravel(BaseModel):
    country: str = Field(min_length=2, examples=['Germany'])
    hotel_class: float = Field(default='', examples=[5.0])
    price: float = Field(ge=0.01, examples=[100.78])
    date: str = Field(examples=['19:00, 25.05.2024'])


class TravelId(BaseModel):
    id: int = Field(description='ID of created travel')


class CreatedProduct(NewTravel, TravelId):
    created_at: datetime
    updated_at: datetime


class DeletedTravel(TravelId):
    status: bool = True
