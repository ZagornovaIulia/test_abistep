from fastapi import status
from typing import Optional


class AppError(Exception):
    """
    Базовый класс для всех ошибок приложения."""
    code: int = status.HTTP_400_BAD_REQUEST
    message: str = "error"

    def __init__(self, message: Optional[str] = None) -> None:
        if message is not None:
            self.message = message


class EmailAlreadyExists(AppError):
    """Ошибка при создании пользователя с уже существующим email."""
    code = status.HTTP_409_CONFLICT
    message = "email already exists"


class UserNotFound(AppError):
    """Ошибка, если пользователь не найден."""
    code = status.HTTP_404_NOT_FOUND
    message = "user not found"


class InsufficientFunds(AppError):
    """Ошибка, если у пользователя недостаточно средств для перевода."""
    code = status.HTTP_400_BAD_REQUEST
    message = "недостаточно средств"


class TransferToSelf(AppError):
    """Ошибка, если пользователь пытается перевести деньги сам себе."""
    code = status.HTTP_400_BAD_REQUEST
    message = "нельзя перевести средства самому себе"
