import logging

from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI
from starlette.requests import Request

from .db import engine
from .models import user  # noqa
from .models.base import Base
from .routes.user import router as user_router
from .settings import PathConfig

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
app.include_router(user_router)
logger = logging.getLogger("app")


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

file_handler = logging.FileHandler(filename=str(PathConfig.log / "app.log"))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

Base.metadata.create_all(bind=engine)


@app.get("/")  # methodとendpointの指定
async def hello():
    return {"text": "hello world!"}


# middleware state.connectionにdatabaseオブジェクトをセットする。
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response
