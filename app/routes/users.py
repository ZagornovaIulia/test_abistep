# app/routes/users.py
from fastapi import APIRouter
from app.errors import EmailAlreadyExists
from app.schema import UserCreate, UserOut
from app import storage

router = APIRouter()


@router.post("/users", response_model=UserOut)
async def create_user(user: UserCreate) -> UserOut:
    """
    Создать нового пользователя.

    returns: UserOut: Созданный пользователь с присвоенным ID.
    """
    users = await storage.get_users()
    if any(u.email == user.email for u in users):
        raise EmailAlreadyExists

    new_id = await storage.get_next_id()
    new_user = UserOut(id=new_id, **user.dict())
    await storage.add_user(new_user)
    return new_user


@router.get("/users", response_model=list[UserOut])
async def list_users() -> list[UserOut]:
    """
    Получить список всех пользователей.

    returns: list[UserOut]: Список пользователей.
    """
    return await storage.get_users()
