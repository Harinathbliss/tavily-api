from fastapi import FastAPI
from routes import router

app = FastAPI(title="Fast API")

app.include_router(router)