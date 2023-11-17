from starlette.responses import JSONResponse
from fastapi import FastAPI

pe_urfu = FastAPI()

@pe_urfu.get("/")
async def root():
    return JSONResponse({"message": "Welcome to Image generator API"})
