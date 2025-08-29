from fastapi import APIRouter
from app.errors import EmailAlreadyExists
from app.schema import UserCreate, UserOut
from app.storage import users, id_generator

router = APIRouter()


@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    if any(u.email == user.email for u in users):
        raise EmailAlreadyExists

    new_user = UserOut(id=next(id_generator), **user.dict())
    users.append(new_user)
    return new_user


@router.get("/users", response_model=list[UserOut])
def list_users():
    return users
