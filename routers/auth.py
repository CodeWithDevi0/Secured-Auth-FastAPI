from fastapi import APIRouter
from pydantic import BaseModel
from services import auth_services

router = APIRouter()

# Define what data the API expects to receive
class UserCredentials(BaseModel):
    username: str
    password: str

@router.post("/api/auth/register")
def register_user(user_data: UserCredentials):
    # Pass the data straight to your service, exactly like your items CRUD!
    return auth_services.register_user_in_db(user_data)

@router.post("/api/auth/login")
def login_user(user_data: UserCredentials):
    # Same here, keep the router thin and let the service do the work
    return auth_services.login_user_in_db(user_data)