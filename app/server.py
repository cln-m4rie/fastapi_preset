import logging

from fastapi import FastAPI

from .routes import user
from .settings import PathConfig

app = FastAPI()
app.include_router(user.router)
logger = logging.getLogger("app")

handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))
handler2 = logging.FileHandler(filename=str(PathConfig.log / "app.log"))  # handler2はファイル出力
handler2.setLevel(logging.DEBUG)  # handler2はLevel.WARN以上
handler2.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logger.addHandler(handler1)
logger.addHandler(handler2)


@app.get("/")  # methodとendpointの指定
async def hello():
    logger.debug("test")
    return {"text": "hello world!"}
