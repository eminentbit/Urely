from django.shortcuts import render

# Create your views here.
def index(request):
    return 'Hello world'

from fastapi import FastAPI
from app.users import router as user_router

app = FastAPI()

# Include the user routes
app.include_router(user_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}