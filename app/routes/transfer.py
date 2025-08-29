from fastapi import APIRouter
from app.errors import TransferToSelf, UserNotFound, InsufficientFunds
from app.storage import users
from app.schema import Transfer, TransferResult

router = APIRouter()


@router.post("/transfer", response_model=TransferResult)
def transfer_money(transfer: Transfer):
    if transfer.from_user_id == transfer.to_user_id:
        raise TransferToSelf

    from_user = next((u for u in users if u.id == transfer.from_user_id), None)
    to_user = next((u for u in users if u.id == transfer.to_user_id), None)

    if not from_user or not to_user:
        raise UserNotFound

    if from_user.balance < transfer.amount:
        raise InsufficientFunds

    from_user.balance -= transfer.amount
    to_user.balance += transfer.amount

    return TransferResult(
        from_user_id=from_user.id,
        to_user_id=to_user.id,
        amount=transfer.amount,
        from_balance=from_user.balance,
        to_balance=to_user.balance,
    )
