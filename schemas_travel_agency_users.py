from pydantic import BaseModel, Field, EmailStr


class NewUser(BaseModel):
    name: str = Field(max_length=50, min_length=1, examples=["Victor"], description='Name of the new user')
    email: EmailStr = Field(examples=['travel_agency2024@ukr.net'], description='Email of the user')


class UserPassword(BaseModel):
    password: str = Field(description="Your password", examples=['12345678'], min_length=8)


class RegisterUserRequest(NewUser, UserPassword):
    pass
