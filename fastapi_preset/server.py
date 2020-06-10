from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/health")
def health_check() -> JSONResponse:
    return JSONResponse(content={"msg": "ok"}, status_code=200)
