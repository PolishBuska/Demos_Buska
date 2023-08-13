from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routers import Songs_router, User_router

app = FastAPI(
    title="Demos_Buska",
    description="This service provides with my own tracks"
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(Songs_router.router)
app.include_router(User_router.router)
@app.get('/')
async def root():
    return "Hello world"



