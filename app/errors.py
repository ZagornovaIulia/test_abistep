from fastapi import status
from typing import Optional


class AppError(Exception):
    code: int = status.HTTP_400_BAD_REQUEST
    message: str = "error"

    def __init__(self, message: Optional[str] = None):
        if message is not None:
            self.message = message


class EmailAlreadyExists(AppError):
    code = status.HTTP_409_CONFLICT
    message = "email already exists"


class UserNotFound(AppError):
    code = status.HTTP_404_NOT_FOUND
    message = "user not found"


class InsufficientFunds(AppError):
    code = status.HTTP_400_BAD_REQUEST
    message = "недостаточно средств"


class TransferToSelf(AppError):
    code = status.HTTP_400_BAD_REQUEST
    message = "нельзя перевести средства самому себе"
