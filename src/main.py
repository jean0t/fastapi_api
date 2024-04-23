from fastapi import FastAPI
from routers import api_router

app = FastAPI(title="SimpleAPI")
app.include_router(api_router)
