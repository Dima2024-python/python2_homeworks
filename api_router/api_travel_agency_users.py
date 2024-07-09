import uuid

from fastapi import HTTPException, APIRouter, Request
from starlette import status
import dao_travel_agency

from schemas_travel_agency_users import RegisterUserRequest, NewUser
from utils.email_sender import create_welcome_letter, send_email


api_router_travel_agency_users = APIRouter(
    prefix='/api/users',
    tags=["API Users"]
)


@api_router_travel_agency_users.post("/verify/", status_code=status.HTTP_201_CREATED)
def create_user(request: Request, new_user: RegisterUserRequest) -> NewUser:
    print(request.__dict__)
    maybe_user = dao_travel_agency.get_user_by_email(new_user.email)
    if maybe_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')

    created_user = dao_travel_agency.create_user(**new_user.dict())
    email_body = create_welcome_letter({
        'name': created_user.name,
        'link': f'{request.base_url}api/users/verify/{created_user.user_uuid}'
    })
    send_email([created_user.email], mail_body=email_body, mail_subject='Verification')
    return created_user


@api_router_travel_agency_users.get("/verify/{user_uuid}")
def verify_user(user_uuid: uuid.UUID):
    maybe_user = dao_travel_agency.get_user_by_uuid(user_uuid)
    if not maybe_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Wrong data')
    dao_travel_agency.activate_account(maybe_user)
    return {'Verified': True, 'user': maybe_user.email}
