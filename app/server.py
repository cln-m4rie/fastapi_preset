import logging

from fastapi import FastAPI

from .routes import user
from .settings import PathConfig

app = FastAPI()
app.include_router(user.router)
logger = logging.getLogger("app")


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

file_handler = logging.FileHandler(filename=str(PathConfig.log / "app.log"))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


@app.get("/")  # methodとendpointの指定
async def hello():
    logger.debug("test")
    return {"text": "hello world!"}
