from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    balance: float = Field(ge=0)


class UserOut(UserCreate):
    id: int


class Transfer(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float = Field(gt=0)


class TransferResult(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float
    from_balance: float
    to_balance: float
