from fastapi import FastAPI
from dotenv import load_dotenv 
load_dotenv(".env")
from routes import base #after loading dotenv because base uses it

app = FastAPI()

app.include_router(base.base_router)