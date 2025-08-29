from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.users import router as users_router
from app.routes.transfer import router as transfer_router
from app.errors import AppError
app = FastAPI()


@app.exception_handler(AppError)
def app_error_handler(_, exc: AppError):
    return JSONResponse(status_code=exc.code, content={"detail": exc.message})


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(users_router)
app.include_router(transfer_router)
