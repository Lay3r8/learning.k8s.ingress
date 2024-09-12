from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from config.settings import get_settings


app = FastAPI()
settings = get_settings()
router = APIRouter(prefix=settings.API_PREFIX)

print(f"API_PREFIX: {settings.API_PREFIX} - VERSION: {settings.VERSION}")


@router.get("/hello")
def hello():
    return {"message": "Hello World!"}


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "Not Found", "API_PREFIX": settings.API_PREFIX},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


app.include_router(router)
