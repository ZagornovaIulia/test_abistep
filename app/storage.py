import asyncio
from itertools import count
from typing import List
from app.schema import UserOut

users: List[UserOut] = []

users_lock = asyncio.Lock()
id_lock = asyncio.Lock()

id_generator = count(1)


async def add_user(user: UserOut) -> None:
    """
    Добавляет пользователя в список `users` под блокировкой.
    """
    async with users_lock:
        users.append(user)

async def get_users() -> List[UserOut]:
    """
    Возвращает копию списка пользователей под блокировкой.
    
    return: Список пользователей.
    """
    async with users_lock:
        return list(users)

async def get_next_id() -> int:
    """
    Генерирует следующий уникальный идентификатор пользователя
    под блокировкой (чтобы избежать гонок при конкурентных вызовах).

    return: int: Следующее значение ID.
    """
    async with id_lock:
        return next(id_generator)
