from pydantic import BaseModel, Field


class NewTravel(BaseModel):
    country: str = Field(max_length=50, min_length=2, examples=["Ukraine"])
    hotel_class: float = Field(default="", examples=[4.5, 5.0])
    price: float = Field(ge=1.0, examples=[20000.96])
    date_start: str = Field(examples=["19:00, 09.06.2023"])
    date_end: str = Field(examples=["19:00, 09.06.2023"])


class TravelId(NewTravel):
    id: int = Field(description="Number of your trip")
