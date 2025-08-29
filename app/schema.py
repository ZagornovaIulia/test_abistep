from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Схема для создания пользователя."""
    name: str
    email: EmailStr
    balance: float = Field(ge=0)


class UserOut(UserCreate):
    """Схема для отображения информации о пользователе."""
    id: int


class Transfer(BaseModel):
    """Схема для запроса перевода средств."""
    from_user_id: int
    to_user_id: int
    amount: float = Field(gt=0)


class TransferResult(BaseModel):
    """Схема результата перевода средств."""
    from_user_id: int
    to_user_id: int
    amount: float
    from_balance: float
    to_balance: float
